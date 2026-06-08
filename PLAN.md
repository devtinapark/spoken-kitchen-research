# Research Plan — and the article spine

The goal is two things at once:
1. **Real GTM research** I can actually use for Spoken Kitchen.
2. A **DevRel article** that shows off Nimble's range → gets me hired.

So every phase below maps a *business question* → a *Nimble capability*. That mapping
IS the article. Each phase produces a finding file + the raw Nimble output, so the
article can show "here's the command, here's what came back, here's what I learned."

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

## Article structure (draft)

1. **Hook** — building Spoken Kitchen for my own grandmother; couldn't find who else needed it.
2. **The problem with manual market research** — slow, stale, gut-feel.
3. **Setup** — Nimble in ~10 minutes.
4. **Phase walkthroughs** (1–5 above), each: question → Nimble command → real output → insight.
5. **The payoff** — the gap map + my actual GTM decisions (ICP, pricing model, positioning).
6. **Reflection** — what Nimble made trivial that used to take an analyst a week.

## Reproducibility convention (chosen for the article)

Shell-first, with a thin Python analysis layer only where a visual lands the insight:

- `scripts/NN-*.sh` — the exact `nimble` CLI commands per phase. Copy-pasteable; these
  are what the article shows inline. Each writes raw output to `data/raw/`.
- `scripts/analysis/*.py` — pandas, used for exactly two artifacts:
  - `pricing_matrix.py` → normalized competitor pricing table + chart
  - `gap_map.py` → the white-space visual that proves the thesis
- Everything else stays as curated markdown findings in `research/`.

Rationale: shows both "I can drive Nimble" (the CLI commands) and "I can turn data
into a decision" (the two charts) — the DevRel skill set without burying the product.

## Status

- [x] Workspace scaffolded
- [x] Nimble CLI installed + authenticated (standard tier: no `fast`/`--include-answer`)
- [x] Confirm competitor shortlist (use as-is + Nimble expansion)
- [x] Phase 1 — landscape
- [x] Phase 2 — pricing
- [x] Phase 3 — positioning
- [x] Phase 4 — ICP
- [x] Phase 5 — gaps
- [x] Draft article
