#!/usr/bin/env bash
set -euo pipefail

if ! command -v gum >/dev/null 2>&1; then
  echo "gum is required. Install from https://github.com/charmbracelet/gum" >&2
  exit 1
fi

title="$(gum input --prompt "Post title: " --placeholder "My New Post")"
if [[ -z "${title// }" ]]; then
  echo "Title cannot be empty." >&2
  exit 1
fi

slug="$(
  printf "%s" "$title" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g; s/-+/-/g'
)"

if [[ -z "$slug" ]]; then
  echo "Failed to derive slug from title." >&2
  exit 1
fi

date="$(date +%F)"
post_dir="content/posts"
post_path="${post_dir}/${date}-${slug}.md"

if [[ -e "$post_path" ]]; then
  echo "Post already exists: $post_path" >&2
  exit 1
fi

mkdir -p "$post_dir"

cat > "$post_path" <<EOF
---
title: ${title}
date: ${date}
css:
  - ../style/main.css
html-math-method: mathml
---

EOF

editor="${EDITOR:-vim}"
"$editor" "$post_path"
