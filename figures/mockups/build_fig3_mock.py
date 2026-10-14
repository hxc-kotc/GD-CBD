import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mock_helpers import watermark, panel_letter, RNG

fig = plt.figure(figsize=(11, 6.5))
fig.suptitle("Figure 3 — Epilepsy (MOCKUP, speculative — collaborator's figure)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.98)
fig.text(0.02, 0.935, "Entirely guessed structure, modeled on Sharma 2024 Fig. 11 (the platform paper). Not confirmed by the collaborator.",
         fontsize=9, color="#D32F2F", style="italic")
gs = GridSpec(2, 3, figure=fig, hspace=0.55, wspace=0.4, top=0.85, bottom=0.1, left=0.07, right=0.97)

groups = ["SAL", "Free CBD", "GD-CBD"]
colors = ["#111111", "#757575", "#2E7D32"]
x = np.arange(3)

def bar_panel(ax, means, err, ylabel, title):
    ax.bar(x, means, yerr=err, color=colors, width=0.55, capsize=3, edgecolor="white")
    pts = [RNG.normal(m, e * 0.6, 6) for m, e in zip(means, err)]
    for xi, p in zip(x, pts):
        ax.scatter(np.full(len(p), xi) + RNG.uniform(-0.1, 0.1, len(p)), p, color="#444444", s=10, zorder=3)
    ax.set_xticks(x); ax.set_xticklabels(groups, fontsize=7.5)
    ax.set_ylabel(ylabel, fontsize=7.5)
    ax.set_title(title, fontsize=8.5)
    watermark(ax, "MOCK")

ax_a = fig.add_subplot(gs[0, 0])
bar_panel(ax_a, [5.6, 4.3, 4.0], [0.6, 0.7, 0.8], "Severity score", "Max. severity")
panel_letter(ax_a, "a")

ax_b = fig.add_subplot(gs[0, 1])
cats = ["No SE", "SE + died", "SE + survived"]
counts = np.array([[0, 1, 3], [4, 2, 1], [6, 3, 4]])  # rows=cats, cols=groups
bottom = np.zeros(3)
cat_colors = ["#C8E6C9", "#FFCDD2", "#FFF9C4"]
for i, cat in enumerate(cats):
    ax_b.bar(x, counts[i], bottom=bottom, color=cat_colors[i], width=0.55, label=cat, edgecolor="white")
    bottom += counts[i]
ax_b.set_xticks(x); ax_b.set_xticklabels(groups, fontsize=7.5)
ax_b.set_ylabel("Animal count", fontsize=7.5)
ax_b.legend(fontsize=6, frameon=False, loc="upper right")
ax_b.set_title("Outcome category", fontsize=8.5)
watermark(ax_b, "MOCK")
panel_letter(ax_b, "b")

ax_c = fig.add_subplot(gs[0, 2])
bar_panel(ax_c, [85, 55, 30], [15, 12, 10], "Duration (s)", "High-grade seizure duration")
panel_letter(ax_c, "c")

ax_d = fig.add_subplot(gs[1, 0])
bar_panel(ax_d, [1400, 1900, 2700], [250, 400, 500], "Latency (s)", "Latency to first high-grade seizure")
panel_letter(ax_d, "d")

ax_e = fig.add_subplot(gs[1, 1])
bar_panel(ax_e, [6000, 5500, 5800], [900, 1100, 950], "Duration (s)", "Low-grade seizure duration")
panel_letter(ax_e, "e")

ax_f = fig.add_subplot(gs[1, 2])
ax_f.axis("off")
ax_f.text(0.5, 0.5, "Inflammatory markers\n(shared panel, see Figure 5)",
          ha="center", va="center", fontsize=8.5, color="#555555",
          bbox=dict(boxstyle="round", facecolor="#F7F7F7", edgecolor="#9E9E9E"))
panel_letter(ax_f, "f")

fig.text(0.02, 0.015,
         "MOCKUP — all panels fully synthetic. Structure guessed from Sharma 2024 Fig. 11; the collaborator's actual data lock is due ~Nov 7 and may look nothing like this.",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig3_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig3_box_layout.png")
