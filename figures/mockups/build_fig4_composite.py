"""
Figure 4 — ONE composite page, matching the journal convention seen across
all four comparator papers (Sah 2023, Porterfield/Sharma 2023, Sharma 2024,
Gusdon 2022): multi-panel figures built around one theme, lettered subpanels
on a single page, not separate images per chart.

Per the user's decision (2026-10-14): V12 and V13 are the same preparation
and are not broken out by cohort anywhere in the figure, not even in panel
titles - that distinction lives in Methods/Table S1 only. The old panel d
(discovery-vs-new-cohort comparison) is cut entirely: once pooled, there is
no separate "old" and "new" to plot against each other in the main figure.
Panels relettered a-f, contiguous, no gap.

Panels a/d/e/f are boxes (no data yet). Panels b/c use the real V12+V13
data, pooled with no cohort distinction.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from matplotlib.gridspec import GridSpec
from mock_helpers import watermark, status_tag

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#555555",
    "axes.labelcolor": "#222222",
    "xtick.color": "#555555",
    "ytick.color": "#555555",
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

COLOR = {"GD-CBD": "#2E7D32", "CBD": "#757575", "Vehicle": "#111111"}

# V12 + V13 per-animal data, pooled with no cohort distinction drawn anywhere below.
COHORTS = [
    {
        "GD-CBD": ([77.5, 77.5, 77.5],
                   [2.5, 4.5, 23.5, 48.5, 73.5, 100, 124, 146, 169],
                   [[37.385, 42.140, 51.165, 41.385, 66.455, 200.715, 21.260, 40.245, 29.045],
                    [112.735, 447.000, 246.635, 259.855, 104.600, 180.870, 155.615, 129.465, 57.000],
                    [214.325, 26.300, 272.540, 128.225, 259.855, 63.320, 254.885, 74.600, 94.475]]),
        "CBD": ([77.5, 57.8625, 70.815],
                [2.5, 4.5, 23.5, 48.5, 73.5, 100, 124, 146, 169],
                [[47.220, 16.095, 27.585, 8.190, 31.705, 48.625, 29.545, 21.060, 84.315],
                 [25.785, 62.750, 33.330, 105.195, 17.645, 12.315, 43.850, 12.600, 24.530],
                 [31.425, 42.140, 54.875, 66.185, 31.905, 44.855, 30.255, 38.550, 58.655]]),
        "Vehicle": ([70.815, 70.815],
                    [2.5, 4.5, 23.5, 48.5, 73.5, 100, 124, 146, 169],
                    [[27.330, 48.050, 16.390, 27.320, 59.660, 20.490, 54.995, 30.845, 10.425],
                     [22.850, 29.730, 105.285, 40.030, 28.530, 25.105, 22.060, 16.025, 23.650]]),
    },
    {
        "GD-CBD": ([100.31, 102.4, 63.56],
                   [2, 4.5, 22, 45, 68, 92, 116, 140, 163.5],
                   [[5.35, 47.22, 19.94, 86.43, 66.78, 47.22, 86.43, 15.45, 14.75],
                    [9.25, 12.9, 27.55, 47.22, 36.58, 35.55, 66.78, 27.07, 8.62],
                    [16.02, 9.67, 48.25, 86.43, 94.3, 119.08, 111.4, 106.77, 50.3]]),
        "Vehicle": ([30.52, 29.26],
                    [2, 4.5, 22, 45, 68, 92, 116, 140, 163.5],
                    [[6.11, 2.47, 4.43, 10.51, 8.59, 1.92, 7.81, 4.7, 13.29],
                     [1.94, 3.83, 1.47, 3.52, 2.51, 2.35, 5.37, 2.36, 1.91]]),
    },
]
ARM_ORDER = ["Vehicle", "CBD", "GD-CBD"]


def pct_baseline(baselines, values):
    return [[100.0 * v / b for v in series] for b, series in zip(baselines, values)]


def time_weighted_mean_pct(hours, pct_series):
    h = np.array(hours, dtype=float)
    return [np.trapezoid(np.array(s, dtype=float), h) / (h[-1] - h[0]) for s in pct_series]


def box_panel(ax, title, desc, status):
    status_color = {"Have": "#2E7D32", "Partial": "#B8860B", "Box": "#9E9E9E"}
    status_face = {"Have": "#E8F5E9", "Partial": "#FFF8E1", "Box": "#F7F7F7"}
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    rect = patches.FancyBboxPatch((0.03, 0.06), 0.94, 0.88,
                                   boxstyle="round,pad=0.01,rounding_size=0.03",
                                   linewidth=1.3, edgecolor=status_color[status], facecolor=status_face[status])
    ax.add_patch(rect)
    ax.text(0.5, 0.76, title, fontsize=9, fontweight="bold", ha="center", va="top", wrap=True)
    ax.text(0.5, 0.56, desc, fontsize=7.5, ha="center", va="top", wrap=True, color="#333333")
    ax.text(0.91, 0.14, status, fontsize=8, fontweight="bold", ha="right", color=status_color[status])


fig = plt.figure(figsize=(13, 9.0))
fig.suptitle("Figure 4 — Flank-incision efficacy (MOCKUP, composite page)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.99)
gs = GridSpec(3, 12, figure=fig, hspace=0.45, wspace=0.9, top=0.86, bottom=0.15, left=0.05, right=0.97, height_ratios=[1, 1, 0.85])

# Panel a: schematic
ax_a = fig.add_subplot(gs[0, 0:4])
box_panel(ax_a, "Study design / timeline", "Surgery -> single IP dose -> daily von Frey to 168h -> ropivacaine", "Have")
ax_a.text(-0.08, 1.15, "a", transform=ax_a.transAxes, fontsize=13, fontweight="bold")

# Panel b: time course, pooled, individual animals, no cohort distinction drawn
ax_b = fig.add_subplot(gs[0, 4:12])
for cohort in COHORTS:
    for arm in ARM_ORDER:
        if arm not in cohort:
            continue
        baselines, hours, values = cohort[arm]
        for animal in pct_baseline(baselines, values):
            ax_b.plot(hours, animal, color=COLOR[arm], linewidth=1.0, alpha=0.5, marker="o", markersize=2.5)
ax_b.axhline(100, color="#bbbbbb", linewidth=0.7, linestyle=":")
ax_b.set_title("GD-CBD 3 mg/kg vs. free CBD vs. vehicle — individual animals", fontsize=9)
ax_b.set_xlabel("Hours", fontsize=8)
ax_b.set_ylabel("% of baseline")
ax_b.text(-0.07, 1.2, "b", transform=ax_b.transAxes, fontsize=13, fontweight="bold")
handles = [Line2D([0], [0], color=COLOR[a], marker="o", markersize=4, label=a) for a in ARM_ORDER]
fig.legend(handles=handles, loc="upper right", ncol=3, frameon=False, fontsize=8, bbox_to_anchor=(0.97, 0.935))

# Panel c: AUC, pooled
ax_c = fig.add_subplot(gs[1, 0:3])
pooled_vals = {"Vehicle": [], "CBD": [], "GD-CBD": []}
for cohort in COHORTS:
    for arm in ARM_ORDER:
        if arm not in cohort:
            continue
        b, h, v = cohort[arm]
        pooled_vals[arm].extend(time_weighted_mean_pct(h, pct_baseline(b, v)))
rng = np.random.default_rng(0)
xpos = {"Vehicle": 0, "CBD": 1, "GD-CBD": 2}
for arm in ARM_ORDER:
    vals = pooled_vals[arm]
    xs = xpos[arm] + rng.uniform(-0.08, 0.08, size=len(vals))
    ax_c.scatter(xs, vals, color=COLOR[arm], s=28, zorder=3, edgecolor="white", linewidth=0.4)
    ax_c.hlines(np.mean(vals), xpos[arm] - 0.2, xpos[arm] + 0.2, color=COLOR[arm], linewidth=2.2, zorder=2)
ax_c.set_xticks([0, 1, 2])
ax_c.set_xticklabels([f"Veh\n(n={len(pooled_vals['Vehicle'])})", f"CBD\n(n={len(pooled_vals['CBD'])})", f"GD-CBD\n(n={len(pooled_vals['GD-CBD'])})"], fontsize=7.5)
ax_c.set_ylabel("Time-wtd mean, % baseline", fontsize=8)
ax_c.set_title("AUC (pooled)", fontsize=8.5)
ax_c.text(-0.3, 1.18, "c", transform=ax_c.transAxes, fontsize=13, fontweight="bold")

# Panels d, e, f: boxes
ax_d = fig.add_subplot(gs[1, 3:6])
box_panel(ax_d, "Responder analysis", "Animal counts per outcome category\n[template: Sharma 2024 Fig. 11b]", "Box")
ax_d.text(-0.08, 1.18, "d", transform=ax_d.transAxes, fontsize=13, fontweight="bold")

ax_e = fig.add_subplot(gs[1, 6:9])
box_panel(ax_e, "Ropivacaine validation", "Transient reversal of hypersensitivity, day 7", "Box")
ax_e.text(-0.08, 1.18, "e", transform=ax_e.transAxes, fontsize=13, fontweight="bold")

ax_f = fig.add_subplot(gs[1, 9:12])
box_panel(ax_f, "Wound histology", "H&E + injury-marker quantification\n[template: Porterfield Fig. 6c-d]", "Box")
ax_f.text(-0.08, 1.18, "f", transform=ax_f.transAxes, fontsize=13, fontweight="bold")

# Panels g, h: anticipate predicate-literature questions (CBD-field reviewers, not just
# this lab's own precedent) - hepatotoxicity and a locomotor/sedation confound control.
# Neither is a planned assay yet; included so the shape exists if the terminal serum
# turns out to be banked (g) or an open-field check gets added as a cheap bump-up (h).
ax_g = fig.add_subplot(gs[2, 0:6])
groups = ["Vehicle", "CBD", "GD-CBD"]
alt = [38, 42, 40]; alt_err = [6, 7, 6]
ast = [95, 102, 98]; ast_err = [12, 14, 11]
xpos = np.arange(3)
w = 0.32
ax_g.bar(xpos - w / 2, alt, width=w, yerr=alt_err, color="#9E9E9E", capsize=3, label="ALT (U/L)", edgecolor="white")
ax_g.bar(xpos + w / 2, ast, width=w, yerr=ast_err, color="#5B8DB8", capsize=3, label="AST (U/L)", edgecolor="white")
ax_g.axhline(55, color="#9E9E9E", linewidth=0.8, linestyle=":")
ax_g.axhline(130, color="#5B8DB8", linewidth=0.8, linestyle=":")
ax_g.set_xticks(xpos); ax_g.set_xticklabels(groups, fontsize=8)
ax_g.set_ylabel("U/L", fontsize=8)
ax_g.legend(fontsize=7.5, frameon=False)
watermark(ax_g, "MOCK")
ax_g.set_title("Hepatic transaminases, terminal serum (dotted = normal range ceiling)", fontsize=8.5)
ax_g.text(-0.08, 1.18, "g", transform=ax_g.transAxes, fontsize=13, fontweight="bold")
status_tag(ax_g, "Box")

ax_h = fig.add_subplot(gs[2, 6:12])
dist = [48, 44, 41]; dist_err = [9, 8, 7]
ax_h.bar(xpos, dist, width=0.5, yerr=dist_err, color=[COLOR["Vehicle"], COLOR["CBD"], COLOR["GD-CBD"]], capsize=3, edgecolor="white")
ax_h.set_xticks(xpos); ax_h.set_xticklabels(groups, fontsize=8)
ax_h.set_ylabel("Open-field distance (m, 10 min)", fontsize=8)
watermark(ax_h, "MOCK")
ax_h.set_title("Locomotor/sedation control — rules out motor confound in von Frey", fontsize=8.5)
ax_h.text(-0.06, 1.18, "h", transform=ax_h.transAxes, fontsize=13, fontweight="bold")
status_tag(ax_h, "Box")

fig.text(0.02, 0.01,
         "Figure 4. GD-CBD efficacy in flank-incision mechanical allodynia. (a) Study design and dosing timeline. (b) Time course of 50% mechanical withdrawal "
         "threshold (von Frey), individual animals, vehicle vs. free CBD vs. GD-CBD, pooled across the discovery cohort; an independent replication cohort pools "
         "in without cohort distinction once dosed. (c) Area under the threshold-vs-time curve (time-weighted mean, % of baseline), individual animals, same "
         "pooling. (d) Responder analysis: fraction of animals recovering to >=50% of baseline threshold by arm. (e) Ropivacaine positive-control validation of "
         "the mechanical-threshold assay. (f) Wound histology, H&E/IHC with injury-marker quantification. (g) Hepatic transaminases (ALT/AST) from terminal "
         "serum, anticipating the most common CBD-field safety question. (h) Open-field locomotor activity, ruling out a motor-confound explanation for the "
         "von Frey result. "
         "Panels b/c use real V12+V13 data, pooled (n=4 vehicle, 3 CBD, 6 GD-CBD; simplified time-weighted-mean calculation, not the locked rank-based primary "
         "analysis). Panels a/d/e/f are placeholders. Panels g/h are not yet planned assays - included to show the shape if terminal serum is banked (g) or an "
         "open-field check is added (h). V12 and V13 are the same preparation and are not distinguished anywhere in this figure - that detail lives in Methods "
         "and Table S1.",
         fontsize=7, color="#555555", wrap=True)

plt.savefig("/home/user/gd-cbd/figures/mockups/fig4_composite.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig4_composite.png (8 panels: a-h)")
