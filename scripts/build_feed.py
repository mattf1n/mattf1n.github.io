#!/usr/bin/env python3
"""Generate feed.xml RSS from content/posts/*.md."""

import datetime as dt
import html
from pathlib import Path
from typing import Dict, List, Tuple
import subprocess

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "content" / "posts"
OUTPUT = ROOT / "feed.xml"
SITE_URL = "https://mattf1n.github.io"
CHANNEL_TITLE = "Matt Fin's Web Log"


def split_front_matter(text: str) -> Tuple[Dict, List[str]]:
    lines = text.splitlines()
    meta: Dict = {}
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_lines = lines[1:i]
                body_lines = lines[i + 1 :]
                meta = parse_front_matter(fm_lines)
                return meta, body_lines
    return meta, lines


def parse_front_matter(lines: List[str]) -> Dict:
    block = "\n".join(lines)
    try:
        import yaml  # type: ignore
    except Exception:
        yaml = None  # type: ignore

    if yaml:
        try:
            return yaml.safe_load(block) or {}
        except Exception:
            pass

    meta: Dict = {}
    for line in lines:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta


def first_paragraph(lines: List[str]) -> str:
    buf: List[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if buf:
                break
            continue
        if stripped.startswith("#"):
            continue
        buf.append(stripped)
    return " ".join(buf).strip()


def truncate(text: str, limit: int = 240) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0] + "…"


def markdown_to_html(md: str) -> str:
    if not md:
        return ""
    try:
        result = subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "html"],
            input=md,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return html.escape(md)


def load_posts(max_items: int = 30) -> List[Dict]:
    posts = []
    for md in POSTS_DIR.glob("*.md"):
        meta, body_lines = split_front_matter(md.read_text(encoding="utf-8"))
        date_str = str(meta.get("date", md.name[:10]))
        try:
            date = dt.date.fromisoformat(date_str)
        except Exception:
            date = None
        title = meta.get("title") or md.stem
        slug = md.stem
        desc_md = truncate(first_paragraph(body_lines))
        desc_html = markdown_to_html(desc_md)
        posts.append(
            {
                "title": title,
                "slug": slug,
                "date": date,
                "date_str": date_str,
                "description": desc_html,
            }
        )
    posts.sort(key=lambda p: (p["date"] or dt.date.min, p["slug"]), reverse=True)
    return posts[:max_items]


def rfc2822(date: dt.date) -> str:
    dt_obj = dt.datetime.combine(date, dt.time.min, dt.timezone.utc)
    return dt_obj.strftime("%a, %d %b %Y %H:%M:%S %z")


def render(posts: List[Dict]) -> str:
    items = []
    for post in posts:
        link = f"{SITE_URL}/posts/{post['slug']}.html"
        if isinstance(post["date"], dt.date):
            pub_date = rfc2822(post["date"])
        else:
            pub_date = html.escape(post["date_str"])
        desc = post["description"]
        items.append(
            f"""  <item>
    <title>{html.escape(post["title"])}</title>
    <link>{link}</link>
    <guid>{link}</guid>
    <pubDate>{pub_date}</pubDate>
    <description><![CDATA[{desc}]]></description>
  </item>"""
        )
    items_block = "\n".join(items)
    last_build = rfc2822(dt.date.today())
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>{CHANNEL_TITLE}</title>
  <link>{SITE_URL}</link>
  <lastBuildDate>{last_build}</lastBuildDate>
{items_block}
</channel>
</rss>
"""


def main() -> None:
    posts = load_posts()
    OUTPUT.write_text(render(posts), encoding="utf-8")


if __name__ == "__main__":
    main()
