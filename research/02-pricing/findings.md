# Phase 2 — Pricing

**Question:** What do competitors charge, and on what model?
**Nimble capability:** `nimble extract` (pricing pages → markdown) + `nimble search` fallbacks.
**Raw output:** `data/raw/02-*` · **Scripts:** `scripts/02-pricing.sh`, `scripts/analysis/pricing_matrix.py`
**Artifacts:** `data/processed/pricing_matrix.csv`, `assets/pricing_matrix.png`
**Run date:** 2026-06-07

---

## Method

Scraped pricing pages directly with `nimble extract --format markdown`. Where prices
were rendered in JS/images (Remento, CreateMyCookbook, Mixbook), fell back to
`nimble search` and read the price out of result snippets. Normalized everything to a
single "entry price to a usable artifact for one family" number in
`scripts/analysis/pricing_matrix.py`.

> Reproducibility note: `extract`'s `--format` is the *content* format
> (`markdown`/`html`/…), **not** output format — `--format json` errors. Standard-tier
> account, so no `--include-answer`.

## The three pricing models

| Model | Who | Mechanics |
|-------|-----|-----------|
| **Annual subscription, book included** | StoryWorth ($59–199/yr), Remento ($99/yr) | One price buys a year of prompts + one hardcover. Gifting-native. |
| **One-time, per-book print** | CreateMyCookbook ($10–20/bk), Mixbook ($15–57/bk), Heritage Cookbook (free build + print) | Pay per physical book; design tools free or cheap. Volume discounts. |
| **Freemium / SaaS utility** | famfood ($5.95/mo, $49/yr), Culinage (free + POD), Otter ($8–30/mo), DeepL ($9–69/mo) | Recurring; the AI is the product, the artifact is on you. |

## Per-competitor detail (sourced)

- **StoryWorth** — Basic $59–79, Color $109, Unlimited $199; each = 1 yr + one premium hardcover. *(welcome.storyworth.com/storyworth-pricing)*
- **Remento** — $99/yr flat: a year of voice-prompted storytelling + one hardcover. E-book $24.99; extra storyteller $99. *(remento.co)*
- **Storii** — monthly subscription (call-in life-story recording); gift box = 12 months prepaid. *(storii.com)*
- **CreateMyCookbook** — eCookbook $9.94/bk, softcover ~$19.95/bk; price breaks at 5/20 books. *(createmycookbook.com/pricing)*
- **Heritage Cookbook** — free to build, pay to print (per-book). *(heritagecookbook.com)*
- **Mixbook** — per-book by size/pages, hardcover from ~$15; free templates, heavy first-order discounts. *(mixbook.com)*
- **famfood** — free tier; "FamFood PLUS" (AI features) $5.95/mo or $49/yr. Voice recipe capture. *(famfood.app)*
- **Culinage** — free trial + monthly; "Culinage Pro" = print-on-demand cookbooks with profit-sharing for creators. *(culinage.app/pricing)*
- **Otter.ai** — Free; Pro $8.33–16.99/mo; Business $30/user/mo. *(otter.ai/pricing)*
- **DeepL** — Individual $8.74/mo (annual) → Advanced $34.49 → Ultimate $68.99. *(deepl.com/pro)*

## Feature × price cross-cut (the gap, in the data)

From `pricing_matrix.csv`, across all 10 competitors:

- **Bilingual:** only **DeepL** — and it's a raw utility, no book, no recipes.
- **Voice input:** Remento, Storii, famfood, Culinage — but **none bilingual**.
- **Physical book:** legacy + cookbook players — but **none voice→translated**.
- **No single competitor** has bilingual **and** voice **and** a finished book.

## Pricing implication for Spoken Kitchen

- The **gifting price ceiling is anchored at ~$99–199** (StoryWorth/Remento). Buyers
  already accept a three-figure, one-payment, book-included gift. That's the slot.
- Pure per-book ($10–57) and pure utility ($6–69/yr) are **commodity floors** — racing
  there means competing with Mixbook on print and DeepL on translation. Don't.
- **Recommended model:** annual subscription **with book included**, priced in the
  StoryWorth/Remento band ($99–199), justified by the bilingual + elderly-voice work
  that none of them do. The translation/voice cost is real and defensible — it's why the
  price holds above the $10 cookbook floor.

→ Carries into Phase 5 (gap map) as the "premium, justified by capability" position.
