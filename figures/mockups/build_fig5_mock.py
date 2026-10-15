import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mock_helpers import watermark, status_tag, panel_letter, COLOR, RNG

fig = plt.figure(figsize=(11, 7.5))
fig.suptitle("Figure 5 — Inflammatory markers across indications (MOCKUP)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.98)
gs = GridSpec(2, 2, figure=fig, hspace=0.6, wspace=0.4, top=0.88, bottom=0.08, left=0.08, right=0.95)

analytes = ["TNF-α", "IL-6", "IL-1β", "IL-10"]
groups = ["Vehicle", "GD-CBD"]
group_colors = ["#111111", COLOR["GD-CBD"]]


def dotplot(ax, title, species_n):
    xpos = np.arange(len(analytes))
    width = 0.3
    for gi, g in enumerate(groups):
        for ai, a in enumerate(analytes):
            base = -15 if g == "GD-CBD" and ai in (0, 2) else RNG.uniform(-5, 15)
            vals = RNG.normal(base, 8, species_n)
            xs = xpos[ai] + (gi - 0.5) * width + RNG.uniform(-0.05, 0.05, species_n)
            ax.scatter(xs, vals, color=group_colors[gi], s=22, alpha=0.85,
                       label=g if ai == 0 else None, edgecolor="white", linewidth=0.3)
            ax.hlines(np.median(vals), xpos[ai] + (gi - 0.5) * width - 0.12, xpos[ai] + (gi - 0.5) * width + 0.12,
                      color=group_colors[gi], linewidth=2)
    ax.axhline(0, color="#bbbbbb", linewidth=0.8, linestyle=":")
    ax.set_xticks(xpos); ax.set_xticklabels(analytes, fontsize=8)
    ax.set_ylabel("% change from baseline", fontsize=8)
    ax.set_title(title, fontsize=9)
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    watermark(ax)


ax_a = fig.add_subplot(gs[0, 0])
dotplot(ax_a, "Pain: wound + plasma (n=3/arm, 72h satellite)", 3)
panel_letter(ax_a, "a")
status_tag(ax_a, "Box")

ax_b = fig.add_subplot(gs[0, 1])
dotplot(ax_b, "Epilepsy: matched panel (n TBD)", 4)
panel_letter(ax_b, "b")
status_tag(ax_b, "Box")

ax_c = fig.add_subplot(gs[1, :])
xpos = np.arange(len(analytes))
pain_effect = [-32, -18, -25, 12]
epi_effect = [-28, -22, -19, 9]
w = 0.32
ax_c.bar(xpos - w / 2, pain_effect, width=w, color="#2E7D32", alpha=0.85, label="Pain (rat)")
ax_c.bar(xpos + w / 2, epi_effect, width=w, color="#5B8DB8", alpha=0.85, label="Epilepsy (mouse)")
ax_c.axhline(0, color="#999999", linewidth=0.8)
ax_c.set_xticks(xpos); ax_c.set_xticklabels(analytes, fontsize=8.5)
ax_c.set_ylabel("Median % change, GD-CBD vs vehicle", fontsize=8.5)
ax_c.legend(fontsize=8, frameon=False)
ax_c.set_title("Combined summary, two species, same analytes", fontsize=9)
watermark(ax_c)
panel_letter(ax_c, "c")
status_tag(ax_c, "Box")

fig.text(0.02, 0.015,
         "Figure 5. Inflammatory marker response to GD-CBD across pain and epilepsy models. (a) Percent change from baseline in wound/plasma TNF-α, IL-6, IL-1β, "
         "and IL-10, vehicle vs. GD-CBD, flank-incision model (n=3/arm, 72h satellite cohort). (b) Percent change from baseline in the same four analytes, vehicle "
         "vs. GD-CBD, epilepsy model (n TBD). (c) Median percent change (GD-CBD vs. vehicle) for each analyte, side by side across the two models. "
         "All three panels fully synthetic. Panel a depends on the Nov satellite group; panel b entirely on the epilepsy collaborator's data lock (~Nov 7).",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig5_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig5_box_layout.png")
