import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from mock_helpers import watermark, status_tag, panel_letter, empty_box, COLOR, RNG

fig = plt.figure(figsize=(11, 7))
fig.suptitle("Biodistribution — conditional, not a numbered main figure (MOCKUP)", fontsize=13.5, fontweight="bold", x=0.02, ha="left", y=0.98)
fig.text(0.02, 0.925, "Promoted to a main-text figure only if Cy5 QC passes and the effect is strong. Shown here fleshed out so the room sees the shape, not the certainty.",
         fontsize=8.5, color="#D32F2F", style="italic")
gs = GridSpec(2, 2, figure=fig, hspace=0.55, wspace=0.35, top=0.84, bottom=0.16, left=0.08, right=0.95)

# a: schematic - real design, Have
ax_a = fig.add_subplot(gs[0, 0])
empty_box(ax_a, "Study design", "Injured + Cy5-GD-CBD (n=3, 24h) vs injured + vehicle (n=2)\nTissue fluorescence + confocal, paired ipsi/contra", "Have")
panel_letter(ax_a, "a")

# b: tissue fluorescence, ipsi vs contra - mock, paired lines
ax_b = fig.add_subplot(gs[0, 1])
n = 3
ipsi = RNG.normal(850, 150, n)
contra = RNG.normal(220, 60, n)
for i in range(n):
    ax_b.plot([0, 1], [contra[i], ipsi[i]], color="#999999", linewidth=1, zorder=1)
ax_b.scatter(np.zeros(n), contra, color="#757575", s=50, zorder=2, label="Contralateral")
ax_b.scatter(np.ones(n), ipsi, color=COLOR["GD-CBD"], s=50, zorder=2, label="Ipsilateral")
ax_b.set_xticks([0, 1]); ax_b.set_xticklabels(["Contra", "Ipsi"], fontsize=8)
ax_b.set_xlim(-0.4, 1.4)
ax_b.set_ylabel("Fluorescence (a.u./g tissue)", fontsize=8)
watermark(ax_b)
ax_b.set_title("Ex vivo tissue fluorescence, paired", fontsize=9)
panel_letter(ax_b, "b")
status_tag(ax_b, "Box")

# c: confocal colocalization - can't fake microscopy, use a labeled cartoon
ax_c = fig.add_subplot(gs[1, 0])
ax_c.set_xlim(0, 1); ax_c.set_ylim(0, 1); ax_c.axis("off")
ax_c.add_patch(mpatches.Circle((0.3, 0.6), 0.15, color="#555555", alpha=0.3))
ax_c.add_patch(mpatches.Circle((0.3, 0.6), 0.08, color=COLOR["GD-CBD"], alpha=0.6))
ax_c.add_patch(mpatches.Circle((0.65, 0.35), 0.15, color="#555555", alpha=0.3))
ax_c.text(0.5, 0.92, "Confocal colocalization (cartoon, not real imaging)", fontsize=8, ha="center")
ax_c.text(0.3, 0.6, "cell\n+ Cy5", fontsize=6.5, ha="center", va="center")
ax_c.text(0.65, 0.35, "cell\nonly", fontsize=6.5, ha="center", va="center")
ax_c.text(0.5, 0.08, "Wound / DRG / cord, with NeuN or Iba1 co-stain", fontsize=7.5, ha="center", color="#555555")
watermark(ax_c, "MOCK")
panel_letter(ax_c, "c")
status_tag(ax_c, "Box")

# d: quantified uptake, mean fluorescence intensity, n cells stated - mock
ax_d = fig.add_subplot(gs[1, 1])
groups = ["Vehicle", "GD-CBD"]
means = [12, 78]
err = [4, 18]
x = np.arange(2)
ax_d.bar(x, means, yerr=err, color=["#111111", COLOR["GD-CBD"]], width=0.5, capsize=4, edgecolor="white")
ax_d.set_xticks(x); ax_d.set_xticklabels(["Vehicle\n(n=40 cells)", "GD-CBD\n(n=55 cells)"], fontsize=7.5)
ax_d.set_ylabel("Mean fluorescence intensity (a.u.)", fontsize=8)
watermark(ax_d)
ax_d.set_title("Quantified uptake — Sharma-style (n cells, not just animals)", fontsize=8.5)
panel_letter(ax_d, "d")
status_tag(ax_d, "Box")

fig.text(0.02, 0.015,
         "MOCKUP — panel a reflects the real design. Panels b/c/d are fully synthetic, conditional on Cy5 QC passing (~Oct 30) and material in hand (~Nov 6). "
         "If QC fails or the effect is modest/negative, this whole figure is omitted or reduced to one Limitations sentence — per the main plan.",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig_bio_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig_bio_box_layout.png")
