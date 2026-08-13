#!/usr/bin/env python3
"""Build an RSS snapshot of the NWS marine point forecast.

The generated feed is static so it can be served by GitHub Pages. Re-run this
script periodically (for example from CI or cron) to publish new forecasts.
"""
from __future__ import annotations

import hashlib
import html
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime, parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

SOURCE_URL = (
    "https://marine.weather.gov/MapClick.php?FcstType=text&TextType=1"
    "&lat=43.707&lon=-69.448"
)
FEED_URL = "https://mattf.nl/marine-weather.xml"


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.html_parts: list[str] = []
        self.in_forecast = False
        self.depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "div" and "margin:25px" in attributes.get("style", ""):
            self.in_forecast = True
            self.depth = 1
        elif self.in_forecast:
            if tag == "div":
                self.depth += 1
            self.html_parts.append(self.get_starttag_text() or f"<{tag}>")
        if self.in_forecast and tag == "br":
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.in_forecast and tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.in_forecast = False
                return
        if self.in_forecast:
            self.html_parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self.in_forecast:
            self.parts.append(data)
            self.html_parts.append(data)


def parse_forecast(source: str) -> tuple[str, str]:
    parser = TextParser()
    parser.feed(source)
    text = html.unescape("".join(parser.parts))
    # Keep paragraph breaks, but avoid retaining the navigation and markup.
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    text = "\n".join(line for line in lines if line).strip()
    return text, "".join(parser.html_parts).strip()


def update_time(forecast: str) -> datetime:
    match = re.search(r"Last Update:\s*([^\n]+)", forecast, re.I)
    if match:
        raw = match.group(1).strip()
        try:
            parsed = parsedate_to_datetime(raw)
            if parsed.tzinfo is not None:
                return parsed.astimezone(timezone.utc)
        except (TypeError, ValueError):
            pass
        # NWS uses a human-readable timestamp with an abbreviation such as EDT.
        match = re.match(r"(.+?)\s+(EST|EDT|CST|CDT|MST|MDT|PST|PDT)\s+(.+)", raw)
        if match:
            offsets = {"EST": -5, "EDT": -4, "CST": -6, "CDT": -5,
                       "MST": -7, "MDT": -6, "PST": -8, "PDT": -7}
            try:
                parsed = datetime.strptime(
                    f"{match.group(1)} {match.group(3)}", "%I:%M %p %b %d, %Y"
                )
                return parsed.replace(
                    tzinfo=timezone.utc if offsets[match.group(2)] == 0
                    else timezone(timedelta(hours=offsets[match.group(2)]))
                ).astimezone(timezone.utc)
            except ValueError:
                pass
    return datetime.now(timezone.utc)


def cdata(value: str) -> str:
    return "<![CDATA[" + value.replace("]]>", "]]]]><![CDATA[>") + "]] >".replace(" ", "")


def tag(name: str, value: str) -> str:
    return f"<{name}>{escape(value)}</{name}>"


def build(output: Path) -> None:
    request = Request(SOURCE_URL, headers={"User-Agent": "marine-weather-rss/1.0"})
    with urlopen(request, timeout=30) as response:
        source = response.read().decode("utf-8", errors="replace")

    forecast, forecast_html = parse_forecast(source)
    if not forecast or not forecast_html:
        raise RuntimeError("The NWS page did not contain a forecast")
    issued = update_time(forecast)
    fingerprint = hashlib.sha256(forecast.encode()).hexdigest()[:16]
    title_match = re.search(r"NWS Forecast for:\s*(.+?)(?:\n|$)", forecast)
    location = title_match.group(1) if title_match else "43.707, -69.448"

    # Keep the serialized feed stable between polls; the forecast update time
    # changes when the upstream forecast changes and is therefore also the
    # appropriate channel build time.
    built = format_datetime(issued, usegmt=True)
    published = format_datetime(issued, usegmt=True)
    body = "\n".join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0">',
        '<channel>',
        tag("title", f"NWS Marine Forecast — {location}"),
        tag("link", SOURCE_URL),
        tag("description", "NWS marine point forecast for 43.707°N, 69.448°W"),
        tag("lastBuildDate", built),
        '<item>',
        tag("title", f"Marine forecast — {location}"),
        tag("link", SOURCE_URL),
        f'<guid isPermaLink="false">{escape(FEED_URL)}#{fingerprint}</guid>',
        tag("pubDate", published),
        f'<description>{cdata(forecast_html)}</description>',
        '</item>',
        '</channel>',
        '</rss>',
    ])
    output.write_text(body + "\n", encoding="utf-8")


if __name__ == "__main__":
    destination = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("marine-weather.xml")
    build(destination)
    print(f"Wrote {destination}")
