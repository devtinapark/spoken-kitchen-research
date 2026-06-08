# Phase 3 — Positioning

**Question:** How do competitors position & market themselves? Messaging, value props, demand language.
**Nimble capability:** `nimble extract` (homepages → markdown) + `nimble search` (SEO/demand language).
**Raw output:** `data/raw/03-*` · **Script:** `scripts/03-positioning.sh`
**Run date:** 2026-06-07

---

## Method

Extracted competitor homepages and pulled H1/H2 messaging (the markdown sits at
`.data.markdown` in each extract's JSON). Then ran demand-language searches to see how
*buyers* phrase the need — the gap between competitor copy and buyer intent is the
positioning opening.

## Messaging matrix (what each one actually says)

| Competitor | Hero message | Hook | Input | Conspicuously absent |
|------------|--------------|------|-------|---------------------|
| **StoryWorth** | "Help Dad see his life in a whole new light" | Gift occasion (Father's Day), 1M books, 50k reviews | "writing or voice, your choice" | recipes, translation, non-English |
| **Remento** | "his voice, forever at your fingertips" | **Voice-first** + scan-to-listen QR in the book | voice → printed book | recipes, translation, non-English |
| **Heritage Cookbook** | "Create Your Own Custom Cookbook Online" | "heritage" in the *name* only; "for every occasion" | manual typing | voice, translation, real heritage angle |
| **CreateMyCookbook** | "Make Your Own Cookbook — easy!" | Free designer, utility | manual typing | emotion, voice, translation |
| **famfood** | "Erinnerungen schmecken" (memories taste) | German-market personal recipe organizer, AI auto-sort | voice/auto-capture | heirloom/elder framing, translation, EN market |
| **Culinage** | (creator POD cookbooks) | Monetization for food *creators*, not families | voice | family/heirloom framing |

## Three positioning territories — and who owns them

1. **Emotional gifting (owned by StoryWorth/Remento).** Occasion-driven, parent/grandparent,
   English. Remento has staked **"voice"** as its wedge — but for *general life stories*.
2. **Utility cookbook-making (owned by Mixbook/CreateMyCookbook/Heritage).** "Easy, free,
   print." No emotion, no voice, manual data entry.
3. **AI recipe utility (famfood/Culinage).** Convenience/organization or creator monetization.

**No one occupies "emotional gifting × recipes × voice × translation."** Heritage Cookbook
has the *word* but not the product; Remento has the *voice mechanic* but not recipes or
language.

## Demand language — how buyers actually talk (SEO signal)

- **Mortality/urgency:** *"get one for my mum while she's still [here]"* — the buying trigger
  is an aging parent. Gift framing works because it's time-bound.
- **Artifact-loss anxiety:** *"my grandmother's recipe box… how do I keep these handwritten
  recipes?"* — the recipe *card/box* is the emotional object competitors ignore.
- **The immigrant/translation need is real and currently DIY:** buyers are *already*
  pasting recipes into free AI translators — *"Translating recipes… keeping culinary
  traditions alive,"* *"I used free AI to translate a 1905 cookbook."* The need is
  **validated but unproductized** — people hack it because no product owns it.
- **"Heritage language"** is a self-identified identity people search around — but no
  recipe/legacy product speaks to it.

## Positioning recommendation for Spoken Kitchen

- **Wedge:** *"Your grandmother's recipes — in her voice, in both your languages, in a book
  you'll cook from."* Combine Remento's voice mechanic + the cookbook artifact + the
  bilingual layer nobody productizes.
- **Trigger to lean on:** the aging-elder urgency (same as StoryWorth) but pointed at the
  **kitchen/recipe** object, which carries even more sensory memory than a memoir.
- **Counter-position vs. Remento:** "Remento saves his stories; Spoken Kitchen saves *her
  kitchen* — and translates it so your kids can cook it too."
- **Channel implication:** target the immigrant-family + heritage-language communities
  already doing this by hand (Phase 4 ICP).

→ Feeds Phase 4 (where these buyers congregate) and Phase 5 (the white-space map).
