#!/usr/bin/env bash
# Phase 1 — Landscape: discover players across Spoken Kitchen's 3 adjacent categories.
# Standard Nimble tier: lite/deep only, no --include-answer.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p data/raw

run() { # run <slug> <args...>
  local slug="$1"; shift
  echo "→ $slug"
  nimble search "$@" --format json > "data/raw/01-${slug}.json"
}

# --- Category 1: emotional / legacy gifting ---
run legacy-alternatives   --query "StoryWorth alternatives family memoir gift service" --search-depth deep --max-results 10
run legacy-discovery      --query "best services to record parents life story and make a book" --search-depth deep --max-results 10

# --- Category 2: recipe / cookbook creators ---
run cookbook-alternatives --query "create custom family cookbook online print service" --search-depth deep --max-results 10
run cookbook-heritage     --query "preserve family recipes heirloom cookbook maker" --search-depth deep --max-results 10

# --- Category 3: AI transcription + translation ---
run ai-transcribe         --query "AI voice transcription and translation app for interviews" --search-depth deep --max-results 10
run ai-recipe-voice       --query "voice to text recipe app record grandmother cooking" --search-depth deep --max-results 10

# --- Intersection probe: does anyone already serve the exact use case? ---
run intersection          --query "AI bilingual heirloom recipe book from elderly relative voice immigrant family" --search-depth deep --max-results 10

echo "Phase 1 raw output written to data/raw/01-*.json"
