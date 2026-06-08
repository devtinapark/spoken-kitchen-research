# Spoken Kitchen — Market Research (powered by Nimble)

Market research for **Spoken Kitchen**: an AI-powered, bilingual *heirloom recipe book*
for immigrant families. It transcribes and translates the voice of an elderly family
cook into an organized bilingual recipe book — available online and as a physical book.

This repo documents how I used [Nimble](https://nimbleway.com) to do the entire
go-to-market research stack — ideal customer profile, competitor pricing, positioning,
market landscape, and white-space analysis — and synthesized it into a deployable HTML
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
| `data/raw/`               | Raw Nimble JSON output |
| `data/processed/`         | Cleaned CSV / tables |
| `docs/`                   | The final HTML report (`index.html`, GitHub Pages) |
| `scripts/`                | Reproducible Nimble commands |

## Reproducing the research

Requires the Nimble CLI, authenticated:

```bash
nimble --version   # verify install
```

See `PLAN.md` for the full research methodology and which Nimble capability maps to
each research question.

## The final report

The synthesized GTM report (decisions for product + marketing) is a single, self-contained
HTML file with all charts embedded:

- **`docs/index.html`** — open it directly, or deploy via GitHub Pages.

Regenerate it from the processed data and charts:

```bash
python3 -m venv .venv && . .venv/bin/activate && pip install pandas matplotlib
python scripts/analysis/pricing_matrix.py   # pricing matrix + chart
python scripts/analysis/gap_map.py          # capability matrix + gap charts
python scripts/build_report.py              # → docs/index.html
```

## Deploying to GitHub Pages

The report is already laid out for Pages (it lives in `docs/`, with a `.nojekyll` marker).

1. Push to GitHub:
   ```bash
   git add docs && git commit -m "Add GTM report" && git push
   ```
2. In the repo: **Settings → Pages → Build and deployment**.
3. Set **Source = Deploy from a branch**, **Branch = main**, **Folder = /docs**, then Save.
4. The report publishes at `https://<user>.github.io/<repo>/` within a minute.

Because the HTML embeds its images as base64, there are no asset paths to break — the one
file is the whole site.
