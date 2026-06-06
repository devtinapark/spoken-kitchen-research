# Spoken Kitchen — Market Research (powered by Nimble)

Market research for **Spoken Kitchen**: an AI-powered, bilingual *heirloom recipe book*
for immigrant families. It transcribes and translates the voice of an elderly family
cook into an organized bilingual recipe book — available online and as a physical book.

This repo documents how I used [Nimble](https://nimbleway.com) to do the entire
go-to-market research stack — ideal customer profile, competitor pricing, positioning,
market landscape, and white-space analysis — and turned it into a DevRel article.

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
| `article/`                | The DevRel article draft |
| `scripts/`                | Reproducible Nimble commands |

## Reproducing the research

Requires the Nimble CLI, authenticated:

```bash
nimble --version   # verify install
```

See `PLAN.md` for the full research methodology and which Nimble capability maps to
each research question.
