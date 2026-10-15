"""
Figure 3 — real collaborator data, from CRS2025SpeakerSlides_-CBD_data_7_2_2025.pptx
(uploaded 2026-10-15). Replaces the earlier fully-speculative Figure 3 mockup
(build_fig3_mock.py / fig3_box_layout.png), now that the collaborator has shared
actual figures instead of a guessed structure.

Source: two composite images embedded in the collaborator's slides 3 and 4,
cropped here into their 7 data panels, plus the real dosing schematic as panel a, relettered a-h, contiguous,
matching the journal composite-figure convention used throughout this figure set.
The collaborator's own color coding (red=Pilo/Sal, green=Pilo/CBD, blue=Pilo/GD-CBD)
is preserved as-is from the source images — not redrawn in our house palette,
since these are the collaborator's real plots, not something we're generating.

The collaborator says more data is still coming (this is not the final panel set
or the final n) — flagged in the caption and in each status tag.
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.gridspec import GridSpec
from mock_helpers import panel_letter, status_tag

SRC = "/home/user/gd-cbd/literature/collaborator_figures"

fig = plt.figure(figsize=(14, 6.8))
fig.suptitle("Figure 3 — GD-CBD reduces seizure severity and improves survival after pilocarpine SE", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.99)
fig.text(0.02, 0.955, "Source: collaborator's slides (CRS 2025), 7/2/25 draft. Colors are the collaborator's own (red=Pilo/Sal, green=Pilo/CBD, blue=Pilo/GD-CBD).",
         fontsize=8.5, color="#555555", style="italic")
# Column spans are sized to each image's own aspect ratio (wide schematic vs. narrow
# portrait bar charts vs. the squarer timecourse/KM panels) so panels pack tightly
# instead of each sitting in an oversized box with empty flanking space.
gs = GridSpec(2, 12, figure=fig, hspace=0.45, wspace=0.25, top=0.89, bottom=0.15, left=0.02, right=0.99)

panels = [
    ("s2_panel_schematic.png", gs[0, 0:5], "a"),
    ("s3_panel1_total_duration.png", gs[0, 5:7], "b"),
    ("s3_panel2_pct_generalized.png", gs[0, 7:9], "c"),
    ("s3_panel3_timecourse.png", gs[0, 9:12], "d"),
    ("s4_panel1_survival48h.png", gs[1, 0:2], "e"),
    ("s4_panel2_km_curve.png", gs[1, 2:6], "f"),
    ("s4_panel3_stacked_stages.png", gs[1, 6:9], "g"),
    ("s4_panel4_stage6.png", gs[1, 9:12], "h"),
]

for fname, slot, letter in panels:
    ax = fig.add_subplot(slot)
    img = mpimg.imread(f"{SRC}/{fname}")
    ax.imshow(img)
    ax.axis("off")
    panel_letter(ax, letter, dx=-0.05, dy=1.02)
    status_tag(ax, "Have")

fig.text(0.02, 0.01,
         "Figure 3. Acute GD-CBD administration reduces seizure duration and severity and improves survival after pilocarpine-induced status epilepticus "
         "(mecp2 model, KO/Het). (a) Dosing and recording timeline: methyl scopolamine, pilocarpine 30 min later, saline/CBD/GD-CBD (30 mg/kg IP) 15 min "
         "after that, 120 min video recording and scoring, then ongoing long-term behavioral studies. (b) Percent total duration seizing. (c) Percent "
         "duration of generalized (stage 3-6) seizures. (d) Percent duration of generalized seizures over time, by 15-min bin. (e) Percent survival at "
         "48h post-SE. (f) Kaplan-Meier probability of survival over 48h. (g) Percent duration of seizure stages, stacked by stage. (h) Percent duration "
         "of stage 6 (most severe) seizure activity. "
         "All panels real data from the collaborator (n as plotted; Pilo/Sal n=11-13, Pilo/CBD n=5, Pilo/GD-CBD n=7, varying slightly by panel). "
         "The collaborator has additional data still to add — this is a draft panel set, not the final n or final figure.",
         fontsize=7, color="#555555", wrap=True)

plt.savefig("/home/user/gd-cbd/figures/mockups/fig3_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig3_box_layout.png (8 panels: a-h, real data)")
