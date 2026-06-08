# Phase 1 — Landscape

**Question:** Who are all the players in each of Spoken Kitchen's 3 adjacent categories?
**Nimble capability:** `nimble search --search-depth deep` discovery sweeps (7 queries).
**Raw output:** `data/raw/01-*.json` · **Script:** `scripts/01-landscape.sh`
**Run date:** 2026-06-07

---

## Method

Seven deep-search discovery sweeps — two per category plus an **intersection probe**
that searched for the exact Spoken Kitchen use case ("AI bilingual heirloom recipe book
from an elderly relative's voice, immigrant family"). The intersection probe is the
thesis test: if a direct competitor exists, it shows up here.

## Category 1 — Emotional / legacy gifting

| Player | Note |
|--------|------|
| **StoryWorth** | Category leader. Weekly prompts → hardcover memoir book. Subscription + book. |
| **Remento** | Shark Tank; voice-recorded prompts → book. Closest "voice" angle in legacy. |
| Storii | Phone-call based story recording (from shortlist; confirmed live). |
| Kindred / Willow / Keepsake Project | Memory/legacy book builders. |
| MyLifeStories, Memorygram, EarlyBird | Aggregators / smaller life-story apps. |

**Read:** crowded, subscription-led, **text-prompt** dominant. Remento is the only one
leaning on *voice* — but it's general life stories, not recipes, not bilingual.

## Category 2 — Recipe / cookbook creators

| Player | Note |
|--------|------|
| **CreateMyCookbook** | Dedicated custom family cookbook → print. |
| **Heritage Cookbook** | "Heritage/heirloom" positioning — closest emotional framing. |
| Mixbook, Shutterfly, Lulu, Greenerprinter | Photo-book / print platforms with cookbook templates. |
| Modern Heirloom Books, Savor, EverPresent | DIY guides + done-for-you recipe-card digitizing. |

**Read:** mature, **print-/template-led**, manual data entry. "Heirloom" language exists
(Heritage Cookbook, EverPresent) but the input is *typing/scanning*, not voice, and
there's no translation.

## Category 3 — AI transcription + translation

| Player | Note |
|--------|------|
| Otter, Sonix, Soniox, Maestra | General transcription (meetings/interviews). |
| Notta, Wordly, DeepL, Google Translate | Translation / multilingual captions. |
| **famfood.app** | ⚠️ *Digitize recipes by voice — no typing.* Closest emerging threat. |
| **culinage.app** | ⚠️ *Voice recordings → cookbook.* Direct-adjacent. |

**Read:** transcription/translation is a commodity layer. The two apps Nimble surfaced
that the shortlist missed — **famfood** and **culinage** — are the real ones to watch:
both apply voice→recipe, but neither is bilingual/translation-first or framed as an
*elderly-relative heirloom* product.

## Intersection probe (the thesis test)

Querying the exact use case returned only **adjacent editorial/community content**
(Edible Communities heirloom-recipe features, a local "Heirloom Collaborative" turning
family recipes into cookbooks) and EverPresent (card digitizing). **No company offers
the full stack:** elderly voice → transcription → bilingual translation → organized
heirloom recipe book (digital + print).

## Takeaways feeding the thesis

1. Each of the 3 categories is real, funded, and active — so the *need* around them is proven.
2. The categories **do not overlap**: legacy=text prompts, cookbook=manual print, AI=commodity utility.
3. **famfood / culinage** are the early movers on voice→recipe — watch closely, but
   neither does bilingual/translation or the elderly-immigrant framing.
4. The intersection is **empty**. White space confirmed at the discovery stage; Phases 2–5
   now size and characterize it.

## Carry-forward competitor set

- **Legacy:** StoryWorth, Remento, Storii
- **Cookbook:** CreateMyCookbook, Heritage Cookbook, Mixbook (+ EverPresent for recipe-card digitizing)
- **AI / direct-adjacent:** famfood.app, culinage.app, Otter (utility baseline), DeepL (translation baseline)
