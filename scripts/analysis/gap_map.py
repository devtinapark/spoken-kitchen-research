#!/usr/bin/env python3
"""Phase 5 analysis — the white-space map that proves the thesis.

Two visuals from the capability data gathered in Phases 1-3:
  1. Capability heatmap: competitors x the 4 capabilities that define the use case.
  2. 2x2 positioning map: emotional-depth (x) vs. bilingual+voice capability (y),
     showing the empty quadrant Spoken Kitchen occupies.

Outputs:
  data/processed/capability_matrix.csv
  assets/gap_heatmap.png
  assets/gap_quadrant.png
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]

# Capabilities that together define the Spoken Kitchen use case.
CAPS = ["Voice input", "Recipe/cookbook", "Bilingual/translation", "Physical book", "Emotional gifting"]
# 1 = yes, 0 = no, 0.5 = partial. Sourced from Phases 1-3 findings.
DATA = {
    "StoryWorth":        [0.5, 0,   0,   1,   1],
    "Remento":           [1,   0,   0,   1,   1],
    "Storii":            [1,   0,   0,   1,   1],
    "CreateMyCookbook":  [0,   1,   0,   1,   0],
    "Heritage Cookbook": [0,   1,   0,   1,   0.5],
    "Mixbook":           [0,   1,   0,   1,   0],
    "famfood":           [1,   1,   0,   0,   0],
    "Culinage":          [0.5, 1,   0,   0.5, 0],
    "Otter.ai":          [1,   0,   0,   0,   0],
    "DeepL":             [0,   0,   1,   0,   0],
    "Spoken Kitchen":    [1,   1,   1,   1,   1],
}
df = pd.DataFrame(DATA, index=CAPS).T
out_csv = ROOT / "data/processed/capability_matrix.csv"
out_csv.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_csv)
print(f"wrote {out_csv}")
df["coverage"] = df.sum(axis=1)
print(df["coverage"].sort_values(ascending=False).to_string())

# --- 1. Heatmap ---
fig, ax = plt.subplots(figsize=(8.5, 6))
m = df[CAPS].values
im = ax.imshow(m, cmap="YlGn", vmin=0, vmax=1, aspect="auto")
ax.set_xticks(range(len(CAPS))); ax.set_xticklabels(CAPS, rotation=30, ha="right", fontsize=9)
ax.set_yticks(range(len(df))); ax.set_yticklabels(df.index, fontsize=9)
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        v = m[i, j]
        ax.text(j, i, {0:"–",0.5:"~",1:"✓"}[v], ha="center", va="center",
                color="#333", fontsize=11, fontweight="bold")
# highlight Spoken Kitchen row
sk = list(df.index).index("Spoken Kitchen")
ax.add_patch(plt.Rectangle((-0.5, sk-0.5), len(CAPS), 1, fill=False, edgecolor="#4f46e5", lw=2.5))
ax.set_title("Capability coverage — only Spoken Kitchen spans all five", fontsize=12)
plt.tight_layout()
p1 = ROOT / "assets/gap_heatmap.png"; plt.savefig(p1, dpi=130); print(f"wrote {p1}")

# --- 2. 2x2 quadrant: emotional gifting (x) vs voice+bilingual capability (y) ---
emo = df["Emotional gifting"] + 0.5*df["Recipe/cookbook"]      # emotional/heirloom depth
cap = df["Voice input"] + df["Bilingual/translation"]          # the hard tech wedge
fig, ax = plt.subplots(figsize=(8.5, 7))
cats = {"StoryWorth":"legacy","Remento":"legacy","Storii":"legacy",
        "CreateMyCookbook":"cookbook","Heritage Cookbook":"cookbook","Mixbook":"cookbook",
        "famfood":"ai","Culinage":"ai","Otter.ai":"ai","DeepL":"ai","Spoken Kitchen":"target"}
col = {"legacy":"#d97706","cookbook":"#2563eb","ai":"#059669","target":"#4f46e5"}
rng = np.random.default_rng(7)
for name in df.index:
    x = emo[name] + rng.uniform(-0.05,0.05)
    y = cap[name] + rng.uniform(-0.05,0.05)
    c = col[cats[name]]
    big = name == "Spoken Kitchen"
    ax.scatter(x, y, s=320 if big else 130, color=c, edgecolor="black",
               zorder=3, marker="*" if big else "o")
    ax.annotate(name, (x, y), xytext=(7,5), textcoords="offset points",
                fontsize=9, fontweight="bold" if big else "normal")
ax.axhspan(1.5, 2.3, xmin=0.62, xmax=1.0, color="#4f46e5", alpha=0.08, zorder=0)
ax.text(1.55, 2.15, "WHITE SPACE", color="#4f46e5", fontweight="bold", fontsize=11)
ax.set_xlabel("Emotional / heirloom depth  →", fontsize=10)
ax.set_ylabel("Voice + bilingual capability  →", fontsize=10)
ax.set_title("The empty quadrant: emotional heirloom × voice+translation", fontsize=12)
ax.set_xlim(-0.2, 2.0); ax.set_ylim(-0.3, 2.4)
ax.grid(True, alpha=0.25)
handles=[plt.Line2D([0],[0],marker='o',color='w',markerfacecolor=col[k],markersize=10,label=v)
         for k,v in {"legacy":"Legacy gifting","cookbook":"Cookbook makers","ai":"AI utility","target":"Spoken Kitchen"}.items()]
ax.legend(handles=handles, loc="lower left", fontsize=8)
plt.tight_layout()
p2 = ROOT / "assets/gap_quadrant.png"; plt.savefig(p2, dpi=130); print(f"wrote {p2}")
