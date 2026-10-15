"""
Figure 3 — real collaborator data, from CRS2025SpeakerSlides_-CBD_data_7_2_2025.pptx
(uploaded 2026-10-15). Replaces the earlier fully-speculative Figure 3 mockup
(build_fig3_mock.py / fig3_box_layout.png), now that the collaborator has shared
actual figures instead of a guessed structure.

Source: two composite images embedded in the collaborator's slides 3 and 4,
cropped here into their 7 individual panels and relettered a-g, contiguous,
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

fig = plt.figure(figsize=(14, 7.2))
fig.suptitle("Figure 3 — GD-CBD reduces seizure severity and improves survival after pilocarpine SE", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.99)
fig.text(0.02, 0.955, "Source: collaborator's slides (CRS 2025), 7/2/25 draft. Colors are the collaborator's own (red=Pilo/Sal, green=Pilo/CBD, blue=Pilo/GD-CBD).",
         fontsize=8.5, color="#555555", style="italic")
gs = GridSpec(2, 12, figure=fig, hspace=0.5, wspace=0.3, top=0.88, bottom=0.17, left=0.03, right=0.98)

panels = [
    ("s3_panel1_total_duration.png", gs[0, 0:3], "a"),
    ("s3_panel2_pct_generalized.png", gs[0, 3:6], "b"),
    ("s3_panel3_timecourse.png", gs[0, 6:12], "c"),
    ("s4_panel1_survival48h.png", gs[1, 0:2], "d"),
    ("s4_panel2_km_curve.png", gs[1, 2:6], "e"),
    ("s4_panel3_stacked_stages.png", gs[1, 6:9], "f"),
    ("s4_panel4_stage6.png", gs[1, 9:12], "g"),
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
         "(mecp2 model, KO/Het). (a) Percent total duration seizing. (b) Percent duration of generalized (stage 3-6) seizures. (c) Percent duration of "
         "generalized seizures over time, by 15-min bin. (d) Percent survival at 48h post-SE. (e) Kaplan-Meier probability of survival over 48h. "
         "(f) Percent duration of seizure stages, stacked by stage. (g) Percent duration of stage 6 (most severe) seizure activity. "
         "All panels real data from the collaborator (n as plotted; Pilo/Sal n=11-13, Pilo/CBD n=5, Pilo/GD-CBD n=7, varying slightly by panel). "
         "The collaborator has additional data still to add — this is a draft panel set, not the final n or final figure.",
         fontsize=7, color="#555555", wrap=True)

plt.savefig("/home/user/gd-cbd/figures/mockups/fig3_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig3_box_layout.png (7 panels: a-g, real data)")
