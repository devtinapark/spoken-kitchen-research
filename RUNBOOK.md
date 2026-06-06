# Manual Runbook — running Nimble yourself

CLI: `@nimble-way/nimble-cli` (installed globally, v0.12.0). It reads `NIMBLE_API_KEY`
from the environment automatically.

## 1. Set your key

Option A — per-shell (temporary):
```bash
export NIMBLE_API_KEY="paste_your_key_here"
```

Option B — repo `.env` (gitignored, persists):
```bash
# .env contains: NIMBLE_API_KEY=your_key
set -a; source .env; set +a
```

## 2. Verify (without printing the key)
```bash
[ -n "$NIMBLE_API_KEY" ] && echo "key loaded (len=${#NIMBLE_API_KEY})" || echo "NOT set"
```

## 3. Smoke test
```bash
nimble search --query "StoryWorth pricing" --max-results 3 --include-answer
```
JSON back = authenticated. `401` = key wrong/inactive.

## 4. Core commands

Search:
```bash
nimble search \
  --query "AI family cookbook for immigrant families" \
  --focus general \
  --search-depth fast \
  --max-results 10 \
  --include-answer
```

Scrape one page (e.g. a pricing page):
```bash
nimble extract --url "https://www.storyworth.com/pricing"
```

Save raw output for the article / pandas:
```bash
nimble search --query "Remento pricing" --search-depth deep --format json \
  > data/raw/remento-pricing.json
```

## Flags worth knowing
- `--format json` — clean machine-readable output (default is `auto`)
- `--search-depth lite|fast|deep` — metadata only / ~2K chars / full scraped page
- `--focus general|news|shopping|...` — search mode
- `-r` / `--raw-output` — print raw string without JSON quotes
- `--debug` — verbose logging when something errors

## Errors
| Status | Meaning | Fix |
|--------|---------|-----|
| 401 | key bad/revoked | re-check key in dashboard, re-export |
| 403 | plan lacks access to that endpoint | check plan in dashboard |
| 429 | rate limited | back off and retry |

Dashboard: https://online.nimbleway.com/settings/api-keys
Docs: https://docs.nimbleway.com/
