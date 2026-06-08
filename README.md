# Spoken Kitchen — Market Research (powered by Nimble)

Market research for **Spoken Kitchen**: an AI-powered, bilingual *heirloom recipe book*
for immigrant families. It transcribes and translates the voice of an elderly family
cook into an organized bilingual recipe book — available online and as a physical book.

This repo documents how I used [Nimble](https://nimbleway.com) to do the entire
go-to-market research stack — ideal customer profile, competitor pricing, positioning,
market landscape, and white-space analysis — and synthesized it into a single HTML
report for product and marketing decisions.

## Why this exists

Spoken Kitchen sits at the intersection of three markets. The research is organized
around proving that the gap between them is real and underserved:

1. **Emotional / legacy products for parents** — e.g. StoryWorth, Remento, Storii
2. **Recipe & cookbook creators (online + physical)** — e.g. CreateMyCookbook, Heritage Cookbook, Paprika
3. **AI transcription + translation apps** — e.g. Otter, Whisper-based tools, DeepL

## Structure

| Path | What's in it |
|------|--------------|
| `research/01-landscape/`  | Competitor discovery across all 3 categories |
| `research/02-pricing/`    | Scraped competitor pricing → comparison matrix |
| `research/03-positioning/`| Messaging, value props, marketing strategy teardown |
| `research/04-icp/`        | Ideal customer profile synthesis |
| `research/05-gaps/`       | White-space / gap analysis (the thesis) |
| `data/raw/`               | Raw Nimble responses (JSON + scraped pages) behind every finding |
| `data/processed/`         | Cleaned CSV / tables |
| `docs/`                   | The final HTML report (`index.html`, GitHub Pages) |
| `scripts/`                | Reproducible Nimble commands |

## The report

The synthesized findings — competitor landscape, pricing, positioning, ICP, and the
white-space thesis, with the product & marketing decisions they imply — are in a single,
self-contained HTML file with all charts embedded:

- **[`docs/index.html`](docs/index.html)** — open it in any browser.

Per-phase detail lives in `research/0N-*/findings.md`; `PLAN.md` maps each business
question to the Nimble capability that answered it.

## Reproducing it

Requires the [Nimble CLI](https://docs.nimbleway.com/) with an API key.

```bash
export NIMBLE_API_KEY="your_key"     # the CLI reads this from the environment
nimble --version                     # verify install
```

> The CLI reads `NIMBLE_API_KEY` from the **environment**, not a `.env` file. If you keep
> it in `.env`, load it first: `set -a; . ./.env; set +a`. Searches here use
> `--search-depth lite|deep` (the `fast` tier and `--include-answer` require an enterprise
> account and otherwise return `403`).

Re-run a phase, then rebuild the charts and report:

```bash
./scripts/01-landscape.sh            # (and 02–04) → raw output in data/raw/

python3 -m venv .venv && . .venv/bin/activate && pip install pandas matplotlib
python scripts/analysis/pricing_matrix.py   # pricing matrix + chart
python scripts/analysis/gap_map.py          # capability matrix + gap charts
python scripts/build_report.py              # → docs/index.html
```
