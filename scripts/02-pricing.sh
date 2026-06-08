#!/usr/bin/env bash
# Phase 2 — Pricing: scrape competitor pricing pages + targeted pricing searches.
# Standard Nimble tier: lite/deep only, no --include-answer.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p data/raw

scrape() { # scrape <slug> <url>  — extract page as markdown
  echo "→ extract $1"
  nimble extract --url "$2" --format markdown -r > "data/raw/02-${1}.md" || echo "  (extract failed for $1)"
}
psearch() { # psearch <slug> <query>
  echo "→ search $1"
  nimble search --query "$2" --search-depth deep --max-results 5 --format json > "data/raw/02-${1}.json"
}

# Direct pricing-page scrapes
scrape storyworth-pricing   "https://welcome.storyworth.com/storyworth-pricing"
scrape remento-pricing      "https://www.remento.co/pricing"
scrape createmycookbook     "https://www.createmycookbook.com/pricing"
scrape heritagecookbook     "https://www.heritagecookbook.com/pricing"
scrape mixbook-cookbook     "https://www.mixbook.com/photo-books/cookbooks"

# Search fallbacks (where a page URL is uncertain or pricing lives off-page)
psearch storii-pricing      "Storii pricing cost per month subscription"
psearch famfood-pricing     "famfood app pricing cost subscription recipe"
psearch culinage-pricing    "Culinage app pricing cost cookbook"
psearch otter-pricing       "Otter.ai pricing plans cost per month 2026"
psearch deepl-pricing       "DeepL pricing plans cost per month 2026"

echo "Phase 2 raw output written to data/raw/02-*.json"
