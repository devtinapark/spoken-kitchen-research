#!/usr/bin/env bash
# Phase 3 — Positioning: scrape competitor homepages for messaging/value props,
# plus SEO/keyword signal via search. Standard tier: lite/deep, no --include-answer.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p data/raw

scrape() { echo "→ extract $1"; nimble extract --url "$2" --format markdown -r > "data/raw/03-${1}.md" 2>&1 || echo "  fail $1"; }
psearch() { echo "→ search $1"; nimble search --query "$2" --search-depth lite --max-results 8 --format json > "data/raw/03-${1}.json"; }

# Homepages — the messaging surface
scrape storyworth-home "https://welcome.storyworth.com/"
scrape remento-home    "https://www.remento.co/"
scrape heritage-home   "https://www.heritagecookbook.com/"
scrape createmy-home   "https://www.createmycookbook.com/"
scrape famfood-home    "https://www.famfood.app/"
scrape culinage-home   "https://www.culinage.app/"

# SEO / demand signal — what language do buyers actually search?
psearch seo-legacy   "gift to record parents life story memories book"
psearch seo-cookbook "how to preserve grandma family recipes cookbook"
psearch seo-immig    "translate family recipes another language keep heritage"

echo "Phase 3 raw output written to data/raw/03-*"
