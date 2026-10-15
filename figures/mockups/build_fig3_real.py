"""
Figure 3 — real collaborator data, from CRS2025SpeakerSlides_-CBD_data_7_2_2025.pptx
(uploaded 2026-10-15). Replaces the earlier fully-speculative Figure 3 mockup
(build_fig3_mock.py / fig3_box_layout.png), now that the collaborator has shared
actual figures instead of a guessed structure.

Source: three images embedded in the collaborator's slides 2-4 (one schematic,
two composite data images), cropped here into 8 individual panels and relettered
a-h, contiguous, matching the journal composite-figure convention used throughout
this figure set. The collaborator's own color coding (red=Pilo/Sal, green=Pilo/CBD,
blue=Pilo/GD-CBD) is preserved as-is from the source images - not redrawn in our
house palette, since these are the collaborator's real plots, not something we're
generating.

Layout: panels are placed with fig.add_axes() at a size computed directly from
each image's own pixel aspect ratio, grouped into two rows by shape (row 1: the
three "wide" plots - schematic, timecourse, KM curve; row 2: the five narrow
portrait bar charts). A GridSpec with uniform row heights forces every panel in
a row into the same box regardless of its native shape, which is what left large
empty margins inside the narrower panels earlier. Computing each panel's box
directly from its aspect ratio (same approach as a bin-packing/tetris layout)
removes that waste - panels differ in size because the source images do, not
because of leftover grid cells.

The collaborator says more data is still coming (this is not the final panel set
or the final n) - flagged in the caption and in each status tag.
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from mock_helpers import panel_letter, status_tag

SRC = "/home/user/gd-cbd/literature/collaborator_figures"

FIG_W, FIG_H = 14.0, 9.3
LEFT_M, RIGHT_M = 0.25, 0.15
TOP_M, BOTTOM_M = 1.2, 0.95   # inches reserved for title/subtitle and caption
ROW_GAP = 0.5
COL_GAP = 0.18

row1 = [
    ("s2_panel_schematic.png", "a"),
    ("s3_panel3_timecourse.png", "b"),
    ("s4_panel2_km_curve.png", "c"),
]
row2 = [
    ("s3_panel1_total_duration.png", "d"),
    ("s3_panel2_pct_generalized.png", "e"),
    ("s4_panel1_survival48h.png", "f"),
    ("s4_panel3_stacked_stages.png", "g"),
    ("s4_panel4_stage6.png", "h"),
]

def aspect(fname):
    w, h = Image.open(f"{SRC}/{fname}").size
    return w / h

avail_w = FIG_W - LEFT_M - RIGHT_M

def row_height(row):
    aspects = [aspect(f) for f, _ in row]
    return (avail_w - (len(row) - 1) * COL_GAP) / sum(aspects)

h1 = row_height(row1)
h2 = row_height(row2)
avail_h = FIG_H - TOP_M - BOTTOM_M
# Scale both rows down together if they don't fit the figure height, preserving
# their relative proportions (h1:h2) rather than letting one row dominate.
scale = min(1.0, avail_h / (h1 + h2 + ROW_GAP))
h1 *= scale
h2 *= scale

fig = plt.figure(figsize=(FIG_W, FIG_H))
fig.suptitle("Figure 3 — GD-CBD reduces seizure severity and improves survival after pilocarpine SE", fontsize=14, fontweight="bold", x=LEFT_M / FIG_W, ha="left", y=0.985)
fig.text(LEFT_M / FIG_W, 1 - 0.62 / FIG_H, "Source: collaborator's slides (CRS 2025), 7/2/25 draft. Colors are the collaborator's own (red=Pilo/Sal, green=Pilo/CBD, blue=Pilo/GD-CBD).",
         fontsize=8.5, color="#555555", style="italic")

y1 = 1 - (TOP_M + h1) / FIG_H
y2 = y1 - ROW_GAP / FIG_H - h2 / FIG_H

for row, y, h in [(row1, y1, h1), (row2, y2, h2)]:
    x = LEFT_M / FIG_W
    for fname, letter in row:
        a = aspect(fname)
        w = h * a
        ax = fig.add_axes([x, y, w / FIG_W, h / FIG_H])
        img = mpimg.imread(f"{SRC}/{fname}")
        ax.imshow(img)
        ax.axis("off")
        panel_letter(ax, letter, dx=-0.04, dy=1.04)
        status_tag(ax, "Have")
        x += (w + COL_GAP) / FIG_W

fig.text(LEFT_M / FIG_W, 0.1 / FIG_H,
         "Figure 3. Acute GD-CBD administration reduces seizure duration and severity and improves survival after pilocarpine-induced status epilepticus "
         "(mecp2 model, KO/Het). (a) Dosing and recording timeline: methyl scopolamine, pilocarpine 30 min later, saline/CBD/GD-CBD (30 mg/kg IP) 15 min "
         "after that, 120 min video recording and scoring, then ongoing long-term behavioral studies. (b) Percent duration of generalized seizures over "
         "time, by 15-min bin. (c) Kaplan-Meier probability of survival over 48h. (d) Percent total duration seizing. (e) Percent duration of generalized "
         "(stage 3-6) seizures. (f) Percent survival at 48h post-SE. (g) Percent duration of seizure stages, stacked by stage. (h) Percent duration of "
         "stage 6 (most severe) seizure activity. "
         "All panels real data from the collaborator (n as plotted; Pilo/Sal n=11-13, Pilo/CBD n=5, Pilo/GD-CBD n=7, varying slightly by panel). "
         "The collaborator has additional data still to add — this is a draft panel set, not the final n or final figure.",
         fontsize=7.5, color="#555555", wrap=True)

plt.savefig("/home/user/gd-cbd/figures/mockups/fig3_box_layout.png", dpi=200)
plt.close()
print(f"Saved fig3_box_layout.png (8 panels: a-h, real data). h1={h1:.2f}in h2={h2:.2f}in scale={scale:.2f}")
