import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mock_helpers import watermark, status_tag, panel_letter, COLOR, RNG

fig = plt.figure(figsize=(11, 4.3))
fig.suptitle("Figure 2 — In vitro activity (MOCKUP)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.99)
gs = GridSpec(1, 3, figure=fig, wspace=0.45, top=0.8, bottom=0.18, left=0.06, right=0.97)

# 2a: TNF-a cytokine panel - mock bars, GD-CBD vs free CBD vs GD alone vs original batch, + viability line
ax_a = fig.add_subplot(gs[0, 0])
groups = ["Vehicle", "GD\nalone", "Free\nCBD", "GD-CBD\n(Batch 4)", "GD-CBD\n(Batch 1)"]
means = [100, 92, 70, 48, 35]
err = [6, 7, 9, 8, 7]
colors = ["#111111", COLOR["GD"], COLOR["CBD"], "#A5D6A7", COLOR["GD-CBD"]]
x = np.arange(len(groups))
ax_a.bar(x, means, yerr=err, color=colors, capsize=3, width=0.6, edgecolor="white")
ax2 = ax_a.twinx()
viability = [98, 96, 95, 94, 93]
ax2.plot(x, viability, color="#D32F2F", marker="D", markersize=4, linewidth=1.2, label="Viability %")
ax2.set_ylim(0, 110); ax2.set_ylabel("Viability (%)", fontsize=7.5, color="#D32F2F")
ax2.tick_params(axis="y", colors="#D32F2F", labelsize=7)
ax_a.set_xticks(x); ax_a.set_xticklabels(groups, fontsize=6.8)
ax_a.set_ylabel("TNF-α release\n(% of LPS-stimulated vehicle)", fontsize=8)
watermark(ax_a)
ax_a.set_title("TNF-α (THP-1), + viability", fontsize=9)
panel_letter(ax_a, "a")
status_tag(ax_a, "Partial")

# 2b: CB1/CB2 binding - mock dose-response curves
ax_b = fig.add_subplot(gs[0, 1])
conc = np.logspace(-3, 2, 50)
def hill(c, ec50, top=100):
    return top * c / (c + ec50)
ax_b.plot(conc, hill(conc, 0.3), color=COLOR["CBD"], linewidth=1.8, label="Free CBD")
ax_b.plot(conc, hill(conc, 7.8), color=COLOR["GD-CBD"], linewidth=1.8, label="GD-CBD")
ax_b.set_xscale("log")
ax_b.set_xlabel("[Compound] (µM)", fontsize=8); ax_b.set_ylabel("CB₂ activation (%)", fontsize=8)
ax_b.legend(fontsize=7, frameon=False)
watermark(ax_b)
ax_b.set_title("CB₂ functional assay", fontsize=9)
panel_letter(ax_b, "b")
status_tag(ax_b, "Box")

# 2c: HU-331 chromatogram - mock
ax_c = fig.add_subplot(gs[0, 2])
t = np.linspace(0, 20, 600)
def peak(center, width, height):
    return height * np.exp(-((t - center) ** 2) / (2 * width ** 2))
trace = peak(8.2, 0.15, 100) + peak(9.6, 0.1, 2.5) + RNG.normal(0, 0.4, len(t))
ax_c.plot(t, trace, color="#111111", linewidth=0.9)
ax_c.annotate("CBD", xy=(8.2, 100), xytext=(8.2, 112), ha="center", fontsize=7)
ax_c.annotate("HU-331?", xy=(9.6, 2.5), xytext=(11, 20), ha="left", fontsize=7,
              arrowprops=dict(arrowstyle="->", color="#D32F2F", lw=0.8), color="#D32F2F")
ax_c.set_xlabel("Retention time (min)", fontsize=8); ax_c.set_ylabel("UV absorbance (a.u.)", fontsize=8)
watermark(ax_c)
ax_c.set_title("HU-331 stability-indicating LC-MS/UV", fontsize=8.5)
panel_letter(ax_c, "c")
status_tag(ax_c, "Box")

fig.text(0.02, 0.01,
         "MOCKUP — panel a bar heights are illustrative, not the real Batch 4 result (some prior TNF-α data exists, due ~Oct 23). "
         "Panels b/c entirely synthetic — CB₂ assay may not happen; HU-331 chromatogram is a plausible shape only, not a real injection.",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig2_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig2_box_layout.png")
