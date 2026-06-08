# Research Plan — and the report spine

The goal:
1. **Real GTM research** for Spoken Kitchen.
2. A **comprehensive HTML report** that turns the findings into product & marketing
   decisions (`docs/index.html`).

So every phase below maps a *business question* → a *Nimble capability*. Each phase
produces a finding file + the raw Nimble output, and the report synthesizes all of it
into "here's what the data says, here's the decision."

## The thesis (what the research must prove)

> Spoken Kitchen lives in the white space between *emotional legacy gifting*,
> *cookbook creation*, and *AI voice→text→translation*. No competitor serves the
> immigrant-family, bilingual, elderly-voice use case end to end. Nimble's web data
> is how I found and sized that gap.

## Phases

| # | Business question | Nimble capability | Output |
|---|-------------------|-------------------|--------|
| 1 | Who are all the players in each of my 3 categories? | `market-finder` / `company-deep-dive` + web search | `research/01-landscape/` |
| 2 | What do competitors charge, and on what model (subscription / one-time / per-book)? | `competitor-positioning` + `nimble-web-expert` (scrape pricing pages) | `research/02-pricing/` |
| 3 | How do they position & market themselves? Messaging, value props, channels, SEO. | `competitor-positioning` + `seo-intel` | `research/03-positioning/` |
| 4 | Who is the ideal customer, and where do they congregate online? | synthesis of 1–3 + targeted `search` (forums, reviews, communities) | `research/04-icp/` |
| 5 | Where is the white space / unmet need? | cross-analysis of all findings | `research/05-gaps/` |

## Competitor shortlist (to confirm before running)

**1. Emotional / legacy products**
- StoryWorth, Remento, Storii, Kindred (family stories), Artkive (kids' art legacy)

**2. Recipe / cookbook creators (online + physical)**
- CreateMyCookbook, Heritage Cookbook, Family Cookbook Project, Paprika, Recipe Keeper, Cooked.wiki

**3. AI transcription + translation**
- Otter.ai, Rev, Whisper-based tools, DeepL, Google Translate, Notta

## Report structure

The synthesized deliverable is `docs/index.html` (self-contained, charts embedded,
GitHub-Pages-ready). Built by `scripts/build_report.py` from the processed data. Sections:

1. **Executive summary** — the thesis, proven; headline stats + decisions.
2. **The opportunity** — capability heatmap + the empty-quadrant gap map.
3. **Phase findings** — landscape, pricing, positioning, customer.
4. **The decision set** — product + marketing decisions, each with its evidence.
5. **Risks & watch list** — what could close the gap.
6. **Methodology** — the reproducible Nimble commands behind every finding.

## Reproducibility convention

Shell-first, with a thin Python analysis layer only where a visual lands the insight:

- `scripts/NN-*.sh` — the exact `nimble` CLI commands per phase. Copy-pasteable; each
  writes raw output to `data/raw/`.
- `scripts/analysis/*.py` — pandas, used for exactly two artifacts:
  - `pricing_matrix.py` → normalized competitor pricing table + chart
  - `gap_map.py` → the white-space visual that proves the thesis
- `scripts/build_report.py` → assembles `docs/index.html` from the processed data.
- Everything else stays as curated markdown findings in `research/`.

## Status

- [x] Workspace scaffolded
- [x] Nimble CLI installed + authenticated (standard tier: no `fast`/`--include-answer`)
- [x] Confirm competitor shortlist (use as-is + Nimble expansion)
- [x] Phase 1 — landscape
- [x] Phase 2 — pricing
- [x] Phase 3 — positioning
- [x] Phase 4 — ICP
- [x] Phase 5 — gaps
- [x] Build HTML report (`docs/index.html`)
