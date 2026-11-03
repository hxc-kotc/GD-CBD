"""
Figure 6 (biodistribution) — REBUILT 2026-11-03 per the 2026-11-02 PI working session.

The old version (build around a new Cy5-GD-CBD dosing study: QC gate, n=3+2,
ipsi/contra fluorescence quantification, a "quantified uptake" bar chart) no
longer matches what was actually decided. Settled at the meeting instead:

- Compound is GD-Cy5 (dendrimer alone, not the CBD conjugate) - "This is not
  GD-CBD-Cy5." The paper is not making a CBD-localization claim, only a
  dendrimer-localization one.
- Material is EXISTING flank-incision cryosections already in hand, not a new
  dosing study. "We're going to just show that and say it's getting into the
  DRG neurons, DRG glia. That's all he looked at." No new animals, no IVIS
  ("we're struggling with IVIS, let's take that out").
- No quantification. "Don't try to quantify or do too much, just show like an
  image and say it's more, it's less, that's good enough."
- A no-dendrimer negative control is wanted alongside the positive images.
- n=3 is the target ("we need to make sure we have N of 3 of the flank
  incision model... for GD-Cy5"), but whether the sections/negative control
  are actually confirmed in hand (vs. needing to be located) is an open
  question - see Open items in the main plan doc. Panel a's design is real
  and settled; panels b/c are schematic placeholders for real images that
  have not been provided to this repo.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from mock_helpers import watermark, status_tag, panel_letter, empty_box

fig = plt.figure(figsize=(11, 5.2))
fig.suptitle("Figure 6 — Biodistribution: GD-Cy5 localization, flank-incision model (MOCKUP)", fontsize=13, fontweight="bold", x=0.02, ha="left", y=0.98)
gs = GridSpec(1, 3, figure=fig, wspace=0.35, top=0.72, bottom=0.22, left=0.05, right=0.97)

# a: schematic - real design, settled 2026-11-02
ax_a = fig.add_subplot(gs[0, 0])
empty_box(ax_a, "Study design", "Existing GD-Cy5 flank-incision cryosections (n=3) +\nno-dendrimer negative control. Localization only,\nno new dosing study, no IVIS.", "Have")
panel_letter(ax_a, "a")

# b: representative positive section - cannot fake a real confocal image, cartoon only
ax_b = fig.add_subplot(gs[0, 1])
ax_b.set_xlim(0, 1); ax_b.set_ylim(0, 1); ax_b.axis("off")
ax_b.add_patch(mpatches.Circle((0.3, 0.6), 0.15, color="#555555", alpha=0.3))
ax_b.add_patch(mpatches.Circle((0.3, 0.6), 0.08, color="#2E7D32", alpha=0.6))
ax_b.add_patch(mpatches.Circle((0.65, 0.35), 0.15, color="#555555", alpha=0.3))
ax_b.text(0.5, 0.95, "Representative GD-Cy5+ (cartoon, not a real image)", fontsize=7.5, ha="center")
ax_b.text(0.3, 0.6, "DRG cell\n+ Cy5", fontsize=6.5, ha="center", va="center")
ax_b.text(0.65, 0.35, "cell\nonly", fontsize=6.5, ha="center", va="center")
ax_b.text(0.5, 0.06, "DRG neurons and glia, representative, not quantified", fontsize=7, ha="center", color="#555555")
watermark(ax_b, "MOCK")
panel_letter(ax_b, "b")
status_tag(ax_b, "Box")

# c: no-dendrimer negative control - same cartoon style, no signal
ax_c = fig.add_subplot(gs[0, 2])
ax_c.set_xlim(0, 1); ax_c.set_ylim(0, 1); ax_c.axis("off")
ax_c.add_patch(mpatches.Circle((0.3, 0.6), 0.15, color="#555555", alpha=0.3))
ax_c.add_patch(mpatches.Circle((0.65, 0.35), 0.15, color="#555555", alpha=0.3))
ax_c.text(0.5, 0.95, "No-dendrimer negative control (cartoon)", fontsize=7.5, ha="center")
ax_c.text(0.3, 0.6, "DRG cell", fontsize=6.5, ha="center", va="center")
ax_c.text(0.65, 0.35, "DRG cell", fontsize=6.5, ha="center", va="center")
ax_c.text(0.5, 0.06, "Same tissue type, no GD-Cy5 dosed", fontsize=7, ha="center", color="#555555")
watermark(ax_c, "MOCK")
panel_letter(ax_c, "c")
status_tag(ax_c, "Box")

fig.text(0.02, 0.02,
         "Figure 6. GD-Cy5 localization after flank-incision injury. (a) Study design: existing cryosections from prior GD-Cy5 dosing, n=3 target, plus a "
         "no-dendrimer negative control. (b) Representative positive section, DRG neurons and glia. (c) Representative no-dendrimer negative control. "
         "Panel a reflects the real, settled design (2026-11-02 PI session): existing material, not a new Cy5-GD-CBD dosing study; no IVIS; no quantification "
         "('just show like an image... that's good enough'). Panels b/c are schematic cartoons standing in for real confocal images not yet provided to this "
         "repo - whether the n=3 sections and negative control are confirmed in hand is an open item (see main plan, Open items).",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig6_biodistribution.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig6_biodistribution.png (3 panels: a-c)")
