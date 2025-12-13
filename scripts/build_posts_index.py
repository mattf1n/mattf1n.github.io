#!/usr/bin/env python3
"""Build a standalone posts index page from content/posts/*.md."""

import datetime as dt
import html
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "content" / "posts"
OUTPUT = ROOT / "posts" / "index.html"


def split_front_matter(text: str) -> Tuple[Dict, List[str]]:
    """Return metadata dict and body lines."""
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
    """Parse YAML-like front matter without external deps."""
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
    """Extract the first non-heading paragraph as markdown."""
    buffer: List[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if buffer:
                break
            continue
        if stripped.startswith("#"):
            continue
        buffer.append(stripped)
    return "\n".join(buffer).strip()


def truncate(text: str, limit: int = 240) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0] + "…"


def markdown_to_html(md: str) -> str:
    """Render markdown to HTML using pandoc; fall back to escaping."""
    if not md:
        return ""
    try:
        result = subprocess.run(
            ["pandoc", "-f", "markdown+emoji", "-t", "html"],
            input=md,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return html.escape(md)


def load_posts() -> List[Dict]:
    posts = []
    for md in sorted(POSTS_DIR.glob("*.md")):
        meta, body_lines = split_front_matter(md.read_text(encoding="utf-8"))
        date_str = str(meta.get("date", md.name[:10]))
        try:
            date = dt.date.fromisoformat(date_str)
        except Exception:
            date = None
        title = meta.get("title") or md.stem
        slug = md.stem
        preview_md = truncate(first_paragraph(body_lines))
        preview_html = markdown_to_html(preview_md)
        posts.append(
            {
                "title": title,
                "slug": slug,
                "date": date,
                "date_str": date_str,
                "preview_html": preview_html,
            }
        )
    posts.sort(key=lambda p: (p["date"] or dt.date.min, p["slug"]), reverse=True)
    return posts


def render_page(posts: List[Dict]) -> str:
    items = []
    for post in posts:
        display_date = (
            post["date"].strftime("%b %d, %Y")
            if isinstance(post["date"], dt.date)
            else html.escape(post["date_str"])
        )
        items.append(
            f"""    <article class="post-card">
      <header>
        <h2><a href="{post["slug"]}.html">{html.escape(post["title"])}</a></h2>
        <time datetime="{html.escape(post["date_str"])}">{display_date}</time>
      </header>
      <div class="preview">
        {post["preview_html"]}
      </div>
    </article>"""
        )
    cards = "\n".join(items) if items else "    <p>No posts yet.</p>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Posts by Matthew Finlayson.">
  <title>Posts · Matt Fin</title>
  <link rel="apple-touch-icon" sizes="180x180" href="/img/fin-180.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/img/fin-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/img/fin-16.png">
  <link rel="manifest" href="../favicon/site.webmanifest">
  <link rel="stylesheet" href="../style/main.css">
  <link rel="stylesheet" href="../style/postindex.css">
</head>
<body>
<header>
  <h1><a href="../index.html">Matthew Finlayson's</a> posts</h1>
  <p>Recent writing, newest first.</p>
</header>
<main>
  <section id="posts-index">
{cards}
  </section>
</main>
</body>
</html>
"""


def main() -> None:
    posts = load_posts()
    html_out = render_page(posts)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html_out, encoding="utf-8")


if __name__ == "__main__":
    main()
