#!/usr/bin/env bash
set -Eeuo pipefail

REPO=/home/matthewf/mattf1n.github.io
LOCK=/tmp/marine-weather-feed.lock

# Prevent overlapping polls/pushes if a network request hangs.
exec 9>"$LOCK"
flock -n 9 || exit 0

cd "$REPO"

tmp=$(mktemp --suffix=.xml)
trap 'rm -f "$tmp"' EXIT
python3 scripts/build_marine_feed.py "$tmp"

# Do not create a commit when the NWS forecast has not changed.
if cmp -s "$tmp" marine-weather.xml; then
    exit 0
fi

mv "$tmp" marine-weather.xml
git add marine-weather.xml
git commit -m "Update marine weather RSS feed"
git push origin master
