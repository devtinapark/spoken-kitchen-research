#!/usr/bin/env python3
"""Phase 2 analysis — normalize competitor pricing into a matrix + chart.

Data is curated from the raw Nimble output in data/raw/02-* (extracts + searches),
with the source URL kept per row for the report's reproducibility.

Outputs:
  data/processed/pricing_matrix.csv
  assets/pricing_matrix.png
"""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]

# entry_usd = realistic entry cost to a finished/usable artifact for one family.
# model: subscription | one-time-per-book | freemium-sub | saas-utility
ROWS = [
    # name, category, model, entry_usd, top_usd, unit, bilingual, voice_input, physical_book, source
    ("StoryWorth",       "legacy",   "subscription",       59,  199, "year + 1 book",  False, False, True,  "welcome.storyworth.com/storyworth-pricing"),
    ("Remento",          "legacy",   "subscription",       99,   99, "year + 1 book",  False, True,  True,  "remento.co/pricing"),
    ("Storii",           "legacy",   "subscription",       15,   15, "month",          False, True,  True,  "storii.com (search)"),
    ("CreateMyCookbook", "cookbook", "one-time-per-book",  10,   20, "per book",       False, False, True,  "createmycookbook.com/pricing"),
    ("Heritage Cookbook","cookbook", "freemium+print",      0,   40, "per book",       False, False, True,  "heritagecookbook.com/pricing"),
    ("Mixbook",          "cookbook", "one-time-per-book",  15,   57, "per book",       False, False, True,  "mixbook.com (search)"),
    ("famfood",          "ai",       "freemium-sub",        6,   49, "mo / year",      False, True,  False, "famfood.app (search)"),
    ("Culinage",         "ai",       "freemium-sub",        0,   49, "mo / year",      False, True,  True,  "culinage.app/pricing"),
    ("Otter.ai",         "ai",       "saas-utility",        8,   30, "month",          False, False, False, "otter.ai/pricing"),
    ("DeepL",            "ai",       "saas-utility",        9,   69, "month",          True,  False, False, "deepl.com/pro"),
    # The product being positioned:
    ("Spoken Kitchen",   "target",   "subscription+book",  None, None,"year + book",   True,  True,  True,  "—"),
]
COLS = ["name","category","model","entry_usd","top_usd","unit",
        "bilingual","voice_input","physical_book","source"]

df = pd.DataFrame(ROWS, columns=COLS)

out_csv = ROOT / "data/processed/pricing_matrix.csv"
out_csv.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_csv, index=False)
print(f"wrote {out_csv}")

# --- Chart: entry price by competitor, colored by category ---
plot = df[df.entry_usd.notna()].sort_values("entry_usd")
colors = {"legacy":"#d97706","cookbook":"#2563eb","ai":"#059669"}
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(plot.name, plot.entry_usd,
               color=[colors[c] for c in plot.category])
for b, v in zip(bars, plot.entry_usd):
    ax.text(v + 1, b.get_y()+b.get_height()/2, f"${int(v)}",
            va="center", fontsize=9)
ax.set_xlabel("Entry price to a usable artifact (USD)")
ax.set_title("Competitor entry pricing — Spoken Kitchen landscape")
handles = [plt.Rectangle((0,0),1,1,color=colors[c]) for c in colors]
ax.legend(handles, ["Legacy gifting","Cookbook makers","AI utility"],
          loc="lower right", fontsize=8)
plt.tight_layout()
out_png = ROOT / "assets/pricing_matrix.png"
out_png.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out_png, dpi=130)
print(f"wrote {out_png}")
