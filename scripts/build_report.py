#!/usr/bin/env python3
"""Build the comprehensive, self-contained HTML GTM report for Spoken Kitchen.

Reads the processed CSVs and the chart PNGs, embeds the images as base64 data URIs,
and writes a single shareable, deployable file: docs/index.html (GitHub Pages root).
"""
from pathlib import Path
import base64, csv

ROOT = Path(__file__).resolve().parents[1]

def img(name):
    p = ROOT / "assets" / name
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/png;base64,{b64}"

def read_csv(name):
    with open(ROOT / "data/processed" / name) as f:
        return list(csv.reader(f))

pricing = read_csv("pricing_matrix.csv")
caps = read_csv("capability_matrix.csv")

CAT_LABEL = {"legacy": "Legacy gifting", "cookbook": "Cookbook makers",
             "ai": "AI utility", "target": "Spoken Kitchen"}

# ---- build capability matrix rows ----
cap_header = caps[0][1:]
def cell(v):
    v = float(v)
    if v == 1.0:  return '<td class="yes">✓</td>'
    if v == 0.5:  return '<td class="part">~</td>'
    return '<td class="no">–</td>'
cap_rows = ""
for row in caps[1:]:
    name = row[0]
    is_sk = name == "Spoken Kitchen"
    cls = ' class="sk-row"' if is_sk else ""
    cells = "".join(cell(v) for v in row[1:])
    total = sum(float(x) for x in row[1:])
    cap_rows += f'<tr{cls}><th>{name}</th>{cells}<td class="score">{total:g}</td></tr>\n'

# ---- build pricing rows ----
def yn(s): return '<span class="chk">✓</span>' if s == "True" else '<span class="dash">–</span>'
price_rows = ""
for row in pricing[1:]:
    name, cat, model, entry, top, unit, bil, voice, book, source = row
    is_sk = cat == "target"
    cls = ' class="sk-row"' if is_sk else ""
    price = "—" if not entry else (f"${float(entry):g}" if entry == top or not top else f"${float(entry):g}–{float(top):g}")
    badge = f'<span class="badge cat-{cat}">{CAT_LABEL.get(cat, cat)}</span>'
    price_rows += (f'<tr{cls}><th>{name}</th><td>{badge}</td><td>{model}</td>'
                   f'<td class="num">{price}</td><td>{unit}</td>'
                   f'<td class="c">{yn(bil)}</td><td class="c">{yn(voice)}</td><td class="c">{yn(book)}</td></tr>\n')

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Spoken Kitchen — GTM Research Report</title>
<style>
  :root {{
    --ink:#0f172a; --muted:#64748b; --line:#e2e8f0; --bg:#ffffff; --card:#ffffff;
    --panel:#f8fafc;
    --accent:#4f46e5; --accent-soft:#eef2ff; --accent-ink:#3730a3;
    --legacy:#b45309; --cookbook:#1d4ed8; --ai:#047857;
    --good:#15803d; --warn:#b45309;
    --maxw:980px;
  }}
  * {{ box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
    font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    -webkit-font-smoothing:antialiased; }}
  .wrap {{ max-width:var(--maxw); margin:0 auto; padding:0 24px; }}
  a {{ color:var(--accent); }}

  /* header */
  header.hero {{ background:var(--panel); border-bottom:1px solid var(--line);
    border-top:3px solid var(--accent); padding:60px 0 48px; }}
  header.hero .wrap {{ max-width:var(--maxw); }}
  .eyebrow {{ letter-spacing:.14em; text-transform:uppercase; font-size:12px; color:var(--accent); font-weight:700; }}
  header.hero h1 {{ font-size:40px; line-height:1.1; margin:12px 0 14px; font-weight:800;
    letter-spacing:-.025em; color:var(--ink); }}
  header.hero p.lede {{ font-size:18px; color:var(--muted); max-width:60ch; margin:0; }}
  .meta {{ margin-top:26px; display:flex; gap:28px; flex-wrap:wrap; font-size:13px; color:var(--muted); }}
  .meta b {{ color:var(--ink); font-weight:600; display:block; font-size:11px; letter-spacing:.06em;
    text-transform:uppercase; color:var(--muted); }}

  /* nav */
  nav.toc {{ position:sticky; top:0; z-index:10; background:rgba(255,255,255,.85);
    backdrop-filter:blur(10px); border-bottom:1px solid var(--line); }}
  nav.toc .wrap {{ display:flex; gap:4px; flex-wrap:wrap; padding:10px 24px; }}
  nav.toc a {{ font-size:13px; font-weight:600; color:var(--muted); text-decoration:none;
    padding:6px 11px; border-radius:7px; transition:background .12s,color .12s; }}
  nav.toc a:hover {{ background:var(--accent-soft); color:var(--accent); }}

  section {{ padding:48px 0; border-bottom:1px solid var(--line); }}
  section h2 {{ font-size:12px; letter-spacing:.12em; text-transform:uppercase; color:var(--accent);
    font-weight:700; margin:0 0 6px; }}
  section h2 + .h {{ font-size:28px; font-weight:800; letter-spacing:-.025em; margin:0 0 18px; line-height:1.15; }}
  section h3 {{ font-size:18px; font-weight:700; margin:30px 0 10px; }}
  p {{ margin:0 0 14px; }} .muted {{ color:var(--muted); }}

  /* exec summary callout */
  .thesis {{ background:var(--panel); border:1px solid var(--line); border-left:3px solid var(--accent);
    border-radius:10px; padding:22px 24px; }}
  .thesis .big {{ font-size:20px; font-weight:700; line-height:1.45; }}

  /* stat strip */
  .stats {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin:24px 0; }}
  .stat {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:18px; }}
  .stat .n {{ font-size:30px; font-weight:800; letter-spacing:-.03em; }}
  .stat .l {{ font-size:13px; color:var(--muted); margin-top:2px; line-height:1.4; }}
  .stat.sk {{ border-color:var(--accent); background:var(--accent-soft); }}
  .stat.sk .n {{ color:var(--accent); }}

  /* cards */
  .grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }}
  .grid3 {{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }}
  .card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:20px; }}
  .card h4 {{ margin:0 0 8px; font-size:16px; }}
  .card.decision {{ border-top:3px solid var(--accent); }}
  .card .tag {{ display:inline-block; font-size:11px; font-weight:700; letter-spacing:.06em;
    text-transform:uppercase; padding:3px 8px; border-radius:6px; margin-bottom:10px; }}
  .tag.product {{ background:var(--accent-soft); color:var(--accent-ink); }}
  .tag.mktg {{ background:#ecfdf5; color:#065f46; }}
  .card .why {{ font-size:13px; color:var(--muted); margin-top:8px; }}

  /* tables */
  .tablewrap {{ overflow-x:auto; border:1px solid var(--line); border-radius:10px; background:var(--card); }}
  table {{ border-collapse:collapse; width:100%; font-size:14px; }}
  th, td {{ padding:10px 12px; text-align:left; border-bottom:1px solid var(--line); }}
  tbody tr:last-child th, tbody tr:last-child td {{ border-bottom:none; }}
  thead th {{ font-size:12px; text-transform:uppercase; letter-spacing:.05em; color:var(--muted);
    background:var(--panel); }}
  tbody th {{ font-weight:600; }}
  td.c, td.num {{ text-align:center; }} td.num {{ font-variant-numeric:tabular-nums; font-weight:600; }}
  td.score {{ text-align:center; font-weight:800; }}
  td.yes {{ background:#ecfdf5; color:#047857; text-align:center; font-weight:700; }}
  td.part {{ background:#fffbeb; color:#b45309; text-align:center; font-weight:700; }}
  td.no {{ background:var(--card); color:#cbd5e1; text-align:center; font-weight:700; }}
  tr.sk-row th, tr.sk-row td {{ background:var(--accent-soft); font-weight:700; }}
  tr.sk-row td.yes {{ background:#c7d2fe; color:var(--accent-ink); }}
  .chk {{ color:var(--good); font-weight:700; }} .dash {{ color:#cbd5e1; }}
  .badge {{ font-size:11px; font-weight:700; padding:3px 8px; border-radius:20px; color:#fff; white-space:nowrap; }}
  .cat-legacy {{ background:var(--legacy); }} .cat-cookbook {{ background:var(--cookbook); }}
  .cat-ai {{ background:var(--ai); }} .cat-target {{ background:var(--accent); }}

  figure {{ margin:18px 0; }}
  figure img {{ width:100%; border:1px solid var(--line); border-radius:10px; background:#fff; }}
  figcaption {{ font-size:13px; color:var(--muted); margin-top:8px; text-align:center; }}

  ul.clean {{ margin:8px 0 14px; padding-left:20px; }} ul.clean li {{ margin:6px 0; }}
  blockquote {{ margin:14px 0; padding:12px 18px; background:var(--panel); border-left:3px solid var(--accent);
    border-radius:0 8px 8px 0; font-style:italic; color:#334155; }}
  .pill {{ display:inline-block; font-size:12px; font-weight:700; padding:4px 10px; border-radius:20px;
    background:var(--accent-soft); color:var(--accent-ink); }}
  code {{ background:var(--panel); border:1px solid var(--line); padding:1px 6px; border-radius:5px; font-size:13px; }}
  footer {{ padding:36px 0 60px; color:var(--muted); font-size:13px; }}

  @media (max-width:720px) {{
    .stats,.grid2,.grid3 {{ grid-template-columns:1fr; }}
    header.hero h1 {{ font-size:30px; }}
  }}
  @media print {{
    nav.toc {{ display:none; }} body {{ background:#fff; }}
    header.hero {{ background:#fff; }}
    section {{ page-break-inside:avoid; }}
  }}
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <div class="eyebrow">Go-to-Market Research · Powered by Nimble</div>
    <h1>Spoken Kitchen: the empty intersection</h1>
    <p class="lede">An AI, bilingual, voice-first heirloom recipe book for immigrant families —
    and the market evidence that no one else is building it.</p>
    <div class="meta">
      <span><b>Prepared</b> 2026-06-07</span>
      <span><b>Method</b> 30+ live Nimble searches & page extracts</span>
      <span><b>Players analyzed</b> 11 across 3 categories</span>
      <span><b>Purpose</b> Product & marketing decisions</span>
    </div>
  </div>
</header>

<nav class="toc"><div class="wrap">
  <a href="#summary">Summary</a>
  <a href="#opportunity">The Opportunity</a>
  <a href="#landscape">Landscape</a>
  <a href="#pricing">Pricing</a>
  <a href="#positioning">Positioning</a>
  <a href="#icp">Customer</a>
  <a href="#decisions">Decisions</a>
  <a href="#risks">Risks &amp; Watch List</a>
  <a href="#method">Method</a>
</div></nav>

<main class="wrap">

<section id="summary">
  <h2>Executive Summary</h2>
  <div class="h">Three crowded markets, one empty cell</div>
  <div class="thesis">
    <p class="big">Spoken Kitchen lives in the white space between <b>emotional legacy gifting</b>,
    <b>cookbook creation</b>, and <b>AI voice→text→translation</b>. Across 11 competitors scored on
    the five capabilities that define the use case, <b>only Spoken Kitchen covers all five</b> —
    and the decisive missing capability across the entire market is <b>bilingual translation</b>.</p>
  </div>
  <div class="stats">
    <div class="stat"><div class="n">11</div><div class="l">competitors analyzed across 3 categories</div></div>
    <div class="stat sk"><div class="n">1</div><div class="l">of 11 covers all 5 capabilities (us)</div></div>
    <div class="stat"><div class="n">0</div><div class="l">competitors pair translation with the recipe use case*</div></div>
    <div class="stat"><div class="n">~20M</div><div class="l">adult 2nd-gen Americans (beachhead segment)</div></div>
  </div>
  <p class="muted">*DeepL offers translation but is a raw utility — no recipe, voice, book, or emotional layer.</p>
  <h3>What this report decides</h3>
  <ul class="clean">
    <li><b>Product:</b> ship the voice → bilingual → cookable heirloom book as one pipeline; translation is the moat.</li>
    <li><b>Pricing:</b> annual subscription, <b>book included, $99–199</b> — the gifting ceiling is already proven.</li>
    <li><b>Positioning:</b> "Her recipes, in her voice, in both your languages." Counter-position to Remento.</li>
    <li><b>Customer & channel:</b> the 2nd-gen "Bridge Daughter"; reach her in community, not paid search.</li>
  </ul>
</section>

<section id="opportunity">
  <h2>The Opportunity</h2>
  <div class="h">The gap, as a picture</div>
  <p>Every competitor was scored on the five capabilities that, combined, define the Spoken Kitchen
  use case. The heatmap makes the moat obvious: the <b>Bilingual / translation</b> column is empty
  for every player except a pure utility (DeepL). No product unites translation with the
  heirloom-recipe job.</p>

  <div class="tablewrap">
    <table>
      <thead><tr><th>Competitor</th>{"".join(f"<th>{h}</th>" for h in cap_header)}<th>Score</th></tr></thead>
      <tbody>{cap_rows}</tbody>
    </table>
  </div>
  <p class="muted" style="margin-top:10px">✓ = full · ~ = partial · – = none. Score is out of 5.</p>

  <figure><img alt="Capability heatmap" src="{img('gap_heatmap.png')}">
    <figcaption>Only Spoken Kitchen spans all five capabilities; the translation column is otherwise empty.</figcaption></figure>

  <figure><img alt="Positioning quadrant" src="{img('gap_quadrant.png')}">
    <figcaption>Emotional/heirloom depth × voice+bilingual capability. The top-right quadrant is empty.</figcaption></figure>

  <p>This is a defensible white space because the missing capability is <b>validated</b> (buyers already
  DIY recipe translation with free AI tools), <b>hard to bolt on</b> (it requires voice → transcription →
  culinary-aware translation → layout), and <b>identity-loaded</b> (it's the exact thing the customer
  fears losing).</p>
</section>

<section id="landscape">
  <h2>Phase 1 · Competitive Landscape</h2>
  <div class="h">Who is already here</div>
  <p>Seven deep discovery searches across the three adjacent categories, plus an intersection probe
  that searched for the exact use case. The categories are real and active — but they do not overlap.</p>
  <div class="grid3">
    <div class="card"><span class="badge cat-legacy">Legacy gifting</span>
      <h4 style="margin-top:10px">StoryWorth · Remento · Storii</h4>
      <p class="muted">Crowded, subscription-led, text-prompt dominant. Remento is the only one leaning
      on <b>voice</b> — but for general life stories, English-only, no recipes.</p></div>
    <div class="card"><span class="badge cat-cookbook">Cookbook makers</span>
      <h4 style="margin-top:10px">CreateMyCookbook · Heritage Cookbook · Mixbook</h4>
      <p class="muted">Mature, print- and template-led, manual data entry. "Heritage" naming exists
      but the input is typing/scanning; no voice, no translation.</p></div>
    <div class="card"><span class="badge cat-ai">AI utility</span>
      <h4 style="margin-top:10px">Otter · DeepL · famfood · Culinage</h4>
      <p class="muted">Commodity transcription/translation. <b>famfood</b> & <b>Culinage</b> (surfaced by
      Nimble, not on the original list) do voice→recipe — the closest movers, but neither is bilingual.</p></div>
  </div>
  <h3>The intersection probe returned nothing direct</h3>
  <p>A search for "AI bilingual heirloom recipe book from an elderly relative's voice, immigrant family"
  surfaced only editorial features and a recipe-card digitizer. The white space is visible at the
  discovery stage and confirmed by the capability scoring above.</p>
</section>

<section id="pricing">
  <h2>Phase 2 · Pricing</h2>
  <div class="h">What the market charges — and what it will pay</div>
  <p>Pricing pages were scraped with <code>nimble extract</code>; JS-rendered prices were recovered via
  search. Three distinct models emerged.</p>
  <div class="tablewrap">
    <table>
      <thead><tr><th>Competitor</th><th>Category</th><th>Model</th><th>Entry</th><th>Unit</th>
        <th>Bilingual</th><th>Voice</th><th>Book</th></tr></thead>
      <tbody>{price_rows}</tbody>
    </table>
  </div>
  <figure><img alt="Entry pricing chart" src="{img('pricing_matrix.png')}">
    <figcaption>Entry price to a usable artifact, by competitor and category.</figcaption></figure>
  <div class="grid3">
    <div class="card"><h4>Subscription + book</h4><p class="muted">StoryWorth $59–199/yr · Remento $99/yr.
      One price = a year of prompts + one hardcover. <b>Gifting-native.</b></p></div>
    <div class="card"><h4>One-time per book</h4><p class="muted">CreateMyCookbook $10–20 · Mixbook $15–57.
      Pay per physical book; design tools free. <b>Commodity floor.</b></p></div>
    <div class="card"><h4>Freemium / SaaS</h4><p class="muted">famfood $49/yr · Otter $8–30/mo · DeepL $9–69/mo.
      The AI is the product; the artifact is on you.</p></div>
  </div>
  <div class="thesis" style="margin-top:18px;border-left-color:var(--good)">
    <p style="margin:0"><b>Pricing decision:</b> price as an <b>annual subscription with the book included,
    in the $99–199 band.</b> Buyers already accept a three-figure, one-payment, book-included gift
    (StoryWorth/Remento). The bilingual + elderly-voice work justifies holding above the $10 cookbook floor;
    racing to the per-book or per-month floor means competing with Mixbook on print and DeepL on translation.</p>
  </div>
</section>

<section id="positioning">
  <h2>Phase 3 · Positioning</h2>
  <div class="h">What they say vs. what buyers want</div>
  <p>Homepages were extracted and their hero messaging compared against how buyers actually phrase the
  need. The gap between the two is the opening.</p>
  <div class="tablewrap">
    <table>
      <thead><tr><th>Competitor</th><th>Hero message</th><th>Hook</th><th>Conspicuously absent</th></tr></thead>
      <tbody>
        <tr><th>StoryWorth</th><td>"Help Dad see his life in a whole new light"</td><td>Gift occasion, 1M books</td><td>recipes, translation, non-English</td></tr>
        <tr><th>Remento</th><td>"his voice, forever at your fingertips"</td><td><b>Voice-first</b> + scan-to-listen</td><td>recipes, translation, non-English</td></tr>
        <tr><th>Heritage Cookbook</th><td>"Create Your Own Custom Cookbook"</td><td>"heritage" in name only</td><td>voice, translation, real heritage angle</td></tr>
        <tr><th>famfood</th><td>"Erinnerungen schmecken" (memories taste)</td><td>German recipe organizer</td><td>heirloom/elder framing, translation, EN market</td></tr>
      </tbody>
    </table>
  </div>
  <h3>How buyers actually talk (demand signal)</h3>
  <ul class="clean">
    <li><b>Mortality/urgency:</b> "get one for my mum while she's still here" — the trigger is an aging parent.</li>
    <li><b>Artifact-loss anxiety:</b> "my grandmother's recipe box… how do I keep these?" — the recipe box is the ignored emotional object.</li>
    <li><b>Translation is already DIY:</b> "I used free AI to translate a 1905 cookbook" — validated, unproductized.</li>
  </ul>
  <div class="thesis" style="margin-top:6px;border-left-color:var(--accent)">
    <p style="margin:0"><b>Positioning decision:</b> <span class="pill">Her recipes, in her voice, in both your languages — in a book you'll cook from.</span>
    Counter-position to Remento: <i>"Remento saves his stories; Spoken Kitchen saves her kitchen — and translates it so your kids can cook it too."</i></p>
  </div>
</section>

<section id="icp">
  <h2>Phase 4 · The Customer</h2>
  <div class="h">Who buys, and where they live online</div>
  <p>The <b>buyer is the adult child (30–50)</b>; the <b>subject is the aging parent</b>. The trigger is
  emotional and time-pressured — the same engine that powers the proven legacy-gifting market.</p>
  <blockquote>"My grandmother passed away last month at 96. While cleaning out her house, nobody had her recipes…"</blockquote>
  <div class="grid2">
    <div class="card">
      <h4>Primary persona — "The Bridge Daughter"</h4>
      <ul class="clean">
        <li><b>Who:</b> 2nd-gen immigrant, 30–50, US, adult child of an aging immigrant parent</li>
        <li><b>Trigger:</b> a parent's health scare, a holiday, a death in the family</li>
        <li><b>Job:</b> capture Mom/Grandma's recipes in her voice & language before they're lost — and make them cookable by English-speaking kids</li>
        <li><b>Pain today:</b> oral or handwritten recipes in another language; manual + DIY AI translation is lossy</li>
        <li><b>Willingness to pay:</b> high — already the $99–199 gift buyer, underserved on language</li>
      </ul>
    </div>
    <div class="card">
      <h4>Where to reach her</h4>
      <ul class="clean">
        <li><b>Reddit</b> — preserving handwritten recipes, grief-over-lost-recipes threads</li>
        <li><b>Facebook Groups</b> — "Preserving family recipes for future generations"</li>
        <li><b>Instagram / YouTube</b> — cultural-heritage cooking creators</li>
        <li><b>Heritage-language & 2nd-gen identity communities</b></li>
        <li><b>Gift-guide surfaces</b> — "gifts for aging parents" intent</li>
      </ul>
      <p class="why">Implication: <b>community-led acquisition</b>, not SEM against Mixbook. Meet buyers in
      the grief/heritage conversations they're already having.</p>
    </div>
  </div>
  <div class="stats" style="grid-template-columns:repeat(3,1fr)">
    <div class="stat"><div class="n">~20M</div><div class="l">adult 2nd-gen Americans (Pew)</div></div>
    <div class="stat"><div class="n">23%</div><div class="l">of US children had an immigrant parent (Census 2009)</div></div>
    <div class="stat"><div class="n">&gt;50%</div><div class="l">immigrant share in some metros — dense & targetable</div></div>
  </div>
</section>

<section id="decisions">
  <h2>The Decision Set</h2>
  <div class="h">What the research tells us to do</div>
  <div class="grid2">
    <div class="card decision"><span class="tag product">Product</span>
      <h4>Build the full pipeline, lead with translation</h4>
      <p>Voice → transcription → bilingual translation → cookable, organized book (digital + print).
      Translation is the one capability no competitor pairs with recipes.</p>
      <p class="why">Evidence: empty bilingual column across all 11 players (Phase 5).</p></div>
    <div class="card decision"><span class="tag mktg">Pricing</span>
      <h4>Annual subscription, book included, $99–199</h4>
      <p>Anchor to the proven gifting ceiling; justify the premium with the voice + translation work.
      Avoid the per-book and per-month commodity floors.</p>
      <p class="why">Evidence: StoryWorth $59–199, Remento $99 (Phase 2).</p></div>
    <div class="card decision"><span class="tag mktg">Positioning</span>
      <h4>"Her recipes, in her voice, in both your languages"</h4>
      <p>Own emotional-heirloom × voice × translation. Counter-position Remento (stories → kitchen) and
      Heritage Cookbook (name → real heritage product).</p>
      <p class="why">Evidence: messaging matrix + DIY-translation demand (Phase 3).</p></div>
    <div class="card decision"><span class="tag mktg">ICP & Channel</span>
      <h4>"Bridge Daughter," reached in community</h4>
      <p>Beachhead on the 2nd-gen adult child of an aging immigrant parent. Lead with content in
      Reddit / Facebook heritage & recipe-preservation communities.</p>
      <p class="why">Evidence: voice-of-customer + ~20M segment (Phase 4).</p></div>
    <div class="card decision"><span class="tag product">Product — MVP wedge</span>
      <h4>Lead feature: the bilingual recipe page</h4>
      <p>The single most differentiating artifact is one recipe shown side-by-side in both languages,
      with a scan-to-hear-her-voice element. Make that the demo.</p>
      <p class="why">Evidence: combines Remento's voice mechanic + the empty translation cell.</p></div>
    <div class="card decision"><span class="tag mktg">Trigger</span>
      <h4>Sell against time, gently</h4>
      <p>The buying moment is "before it's too late." Campaign around holidays and milestone moments;
      frame the product as capturing what's still here.</p>
      <p class="why">Evidence: mortality/urgency language dominates demand (Phase 3/4).</p></div>
  </div>
</section>

<section id="risks">
  <h2>Risks &amp; Watch List</h2>
  <div class="h">What could close the gap</div>
  <div class="grid2">
    <div class="card"><h4>⚠️ famfood &amp; Culinage</h4>
      <p class="muted">The closest movers on voice→recipe. Neither is bilingual or framed for the
      elderly-immigrant heirloom use case <i>yet</i>. Adding a translation layer is their fastest path
      into our space — monitor quarterly.</p></div>
    <div class="card"><h4>⚠️ Remento extends to recipes</h4>
      <p class="muted">Remento already owns the voice mechanic and the gifting brand. A "recipe edition"
      is conceivable — but recipes + translation is a different data pipeline and ICP.</p></div>
    <div class="card"><h4>⚠️ Commodity translation perception</h4>
      <p class="muted">Buyers DIY translation with free AI, which both validates the need and risks
      "why pay?" Mitigate by making translation <i>culinary-aware</i> and inseparable from the book.</p></div>
    <div class="card"><h4>⚠️ Print/fulfillment economics</h4>
      <p class="muted">Cookbook makers compete at $10–57/book. The book is a cost center, not the moat —
      keep print partnered/POD and price the experience, not the paper.</p></div>
  </div>
</section>

<section id="method">
  <h2>Methodology &amp; Reproducibility</h2>
  <div class="h">How this was produced</div>
  <p>Every finding is backed by live web data gathered with the <a href="https://nimbleway.com">Nimble</a>
  CLI. Each phase is a shell script that writes raw JSON to <code>data/raw/</code>; two Python scripts turn
  the data into the charts and matrices embedded above.</p>
  <ul class="clean">
    <li><code>scripts/01-landscape.sh</code> — 7 discovery + intersection searches</li>
    <li><code>scripts/02-pricing.sh</code> — pricing-page extracts + search fallbacks</li>
    <li><code>scripts/03-positioning.sh</code> — homepage extracts + demand searches</li>
    <li><code>scripts/04-icp.sh</code> — voice-of-customer, community, market-size searches</li>
    <li><code>scripts/analysis/pricing_matrix.py</code> · <code>scripts/analysis/gap_map.py</code> — tables &amp; charts</li>
    <li><code>scripts/build_report.py</code> — generates this self-contained HTML</li>
  </ul>
  <p class="muted">Detailed per-phase findings live in <code>research/0N-*/findings.md</code>. Account note:
  standard Nimble tier — searches use <code>--search-depth lite|deep</code> (no <code>fast</code>/<code>--include-answer</code>).</p>
</section>

</main>

<footer><div class="wrap">
  Spoken Kitchen — GTM Research Report · Generated 2026-06-07 from live Nimble web data ·
  Self-contained HTML, charts embedded.
</div></footer>

</body>
</html>
"""

# Deploy target: docs/ is a one-click GitHub Pages source on the main branch.
out = ROOT / "docs/index.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(HTML)
(out.parent / ".nojekyll").write_text("")  # serve the file as-is, skip Jekyll
print(f"wrote {out}  ({len(HTML)//1024} KB)")
