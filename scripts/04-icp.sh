#!/usr/bin/env bash
# Phase 4 — ICP: who is the buyer, and where do they congregate online?
# Standard tier: lite/deep, no --include-answer.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p data/raw

psearch() { echo "→ $1"; nimble search --query "$2" --search-depth deep --max-results 8 --format json > "data/raw/04-${1}.json"; }

# Who feels the pain (communities + voice of customer)
psearch voc-recipes    "reddit preserve grandmother handwritten recipes before she passes"
psearch voc-immigrant  "second generation immigrant losing parents native language recipes"
psearch voc-translate  "translate family recipes English for my kids heritage"

# Where they gather (communities, forums, subreddits, FB groups)
psearch community      "online communities immigrant heritage food family recipes preserve"
psearch gifting        "best sentimental gift for aging immigrant parents grandparents"

# Demographic / market sizing signal
psearch market-size    "number of second generation immigrant households US heritage language"

echo "Phase 4 raw output written to data/raw/04-*.json"
