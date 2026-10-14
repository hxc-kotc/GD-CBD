"""
Figure 4 — ONE composite page, matching the journal convention seen across
all four comparator papers (Sah 2023, Porterfield/Sharma 2023, Sharma 2024,
Gusdon 2022): multi-panel figures built around one theme, lettered subpanels
on a single page, not separate images per chart.

Panels a/e/f/g are boxes (no data yet). Panels b/c/d use the real V12/V13
data, same calculation as build_fig4.py.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from matplotlib.gridspec import GridSpec

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

DATA = {
    "V12 (Dec 2024)": {
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
    "V13 (Jan 2025)": {
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
}
ARM_ORDER = ["Vehicle", "CBD", "GD-CBD"]
COHORT_ORDER = list(DATA.keys())


def pct_baseline(baselines, values):
    return [[100.0 * v / b for v in series] for b, series in zip(baselines, values)]


def time_weighted_mean_pct(hours, pct_series):
    h = np.array(hours, dtype=float)
    return [np.trapezoid(np.array(s, dtype=float), h) / (h[-1] - h[0]) for s in pct_series]


def box_panel(ax, letter, title, desc, status):
    status_color = {"Have": "#2E7D32", "Partial": "#B8860B", "Box": "#9E9E9E"}
    status_face = {"Have": "#E8F5E9", "Partial": "#FFF8E1", "Box": "#F7F7F7"}
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    rect = patches.FancyBboxPatch((0.02, 0.05), 0.96, 0.9,
                                   boxstyle="round,pad=0.01,rounding_size=0.03",
                                   linewidth=1.3, edgecolor=status_color[status], facecolor=status_face[status])
    ax.add_patch(rect)
    ax.text(0.5, 0.78, title, fontsize=9, fontweight="bold", ha="center", va="top", wrap=True)
    ax.text(0.5, 0.58, desc, fontsize=7.5, ha="center", va="top", wrap=True, color="#333333")
    ax.text(0.92, 0.12, status, fontsize=8, fontweight="bold", ha="right", color=status_color[status])


fig = plt.figure(figsize=(13, 9))
fig.suptitle("Figure 4 — Flank-incision efficacy (MOCKUP, composite page)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.99)
gs = GridSpec(3, 6, figure=fig, hspace=0.65, wspace=0.75, top=0.90, bottom=0.08, left=0.06, right=0.97)

# Panel a: schematic (box, but "Have" status - design is set, just needs a drawn diagram)
ax_a = fig.add_subplot(gs[0, 0:2])
box_panel(ax_a, "a", "Study design / timeline", "Surgery -> single IP dose -> daily von Frey to 168h -> ropivacaine", "Have")

# Panel b: time course, V12+V13 treated as one discovery cohort (same preparation,
# Batch 1). Individual animal trajectories shown, not binned to a common timepoint
# grid - V12 and V13 used different von Frey sampling hours, and fabricating a
# shared timeline would overstate precision. No per-cohort distinction drawn.
ax_b = fig.add_subplot(gs[0, 2:6])
for cohort in COHORT_ORDER:
    arms = DATA[cohort]
    for arm in ARM_ORDER:
        if arm not in arms:
            continue
        baselines, hours, values = arms[arm]
        pct = pct_baseline(baselines, values)
        for animal in pct:
            ax_b.plot(hours, animal, color=COLOR[arm], linewidth=1.0, alpha=0.5, marker="o", markersize=2.5)
ax_b.axhline(100, color="#bbbbbb", linewidth=0.7, linestyle=":")
ax_b.set_title("Discovery cohort (V12+V13 pooled) — individual animals", fontsize=9)
ax_b.set_xlabel("Hours", fontsize=8)
ax_b.set_ylabel("% of baseline")
ax_b.text(-0.1, 1.2, "b", transform=ax_b.transAxes, fontsize=13, fontweight="bold")
handles = [Line2D([0], [0], color=COLOR[a], marker="o", markersize=4, label=a) for a in ARM_ORDER]
fig.legend(handles=handles, loc="upper right", ncol=3, frameon=False, fontsize=8, bbox_to_anchor=(0.97, 0.965))

# Panel c: AUC pooled
ax_c = fig.add_subplot(gs[1, 0:2])
pooled_vals = {"Vehicle": [], "CBD": [], "GD-CBD": []}
for cohort in COHORT_ORDER:
    for arm in ARM_ORDER:
        if arm not in DATA[cohort]:
            continue
        b, h, v = DATA[cohort][arm]
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
ax_c.set_title("V12+V13 pooled", fontsize=8.5)
ax_c.text(-0.38, 1.22, "c", transform=ax_c.transAxes, fontsize=13, fontweight="bold")

# Panel d: effect size, discovery (pooled) vs new cohort (pending) — two rows,
# matching the plan's actual replication test (new/independent preparation vs
# the discovery data), not a per-cohort breakdown of V12 vs V13.
ax_d = fig.add_subplot(gs[1, 2:6])
gd_vals_all, ve_vals_all = [], []
for cohort in COHORT_ORDER:
    b_gd, h_gd, v_gd = DATA[cohort]["GD-CBD"]
    b_ve, h_ve, v_ve = DATA[cohort]["Vehicle"]
    gd_vals_all.extend(time_weighted_mean_pct(h_gd, pct_baseline(b_gd, v_gd)))
    ve_vals_all.extend(time_weighted_mean_pct(h_ve, pct_baseline(b_ve, v_ve)))
diff = np.mean(gd_vals_all) - np.mean(ve_vals_all)
se = np.sqrt(np.var(gd_vals_all, ddof=1) / len(gd_vals_all) + np.var(ve_vals_all, ddof=1) / len(ve_vals_all))

ax_d.errorbar([diff], [1], xerr=[1.96 * se], fmt="D", color="#2E7D32", markersize=7, capsize=4, linewidth=1.8, ecolor="#555555")
ax_d.scatter([0], [0], marker="s", s=100, facecolor="#f2f2f2", edgecolor="#9E9E9E", linewidth=1.2, zorder=3)
ax_d.text(0, 0, "?", ha="center", va="center", fontsize=9, color="#9E9E9E", fontweight="bold")
ax_d.axvline(0, color="#999999", linewidth=1, linestyle="--")
ax_d.set_xlim(-30, 200)
ax_d.set_ylim(-0.6, 1.6)
ax_d.set_yticks([0, 1])
ax_d.set_yticklabels(["New — pending", "Discovery (pooled)"], fontsize=8.5)
ax_d.set_xlabel("GD-CBD minus vehicle, % baseline (illustrative CI)", fontsize=8)
ax_d.set_title(f"Discovery vs. replication  —  discovery: GD-CBD n={len(gd_vals_all)}, veh n={len(ve_vals_all)}", fontsize=8.5)
ax_d.text(-0.2, 1.22, "d", transform=ax_d.transAxes, fontsize=13, fontweight="bold")

# Panels e, f, g: boxes
ax_e = fig.add_subplot(gs[2, 0:2])
box_panel(ax_e, "e", "Responder analysis", "Animal counts per outcome category\n[template: Sharma 2024 Fig. 11b]", "Box")
ax_f = fig.add_subplot(gs[2, 2:4])
box_panel(ax_f, "f", "Ropivacaine validation", "Transient reversal of hypersensitivity, day 7", "Box")
ax_g = fig.add_subplot(gs[2, 4:6])
box_panel(ax_g, "g", "Wound histology", "H&E + injury-marker quantification\n[template: Porterfield Fig. 6c-d]", "Box")

fig.text(0.02, 0.015,
         "MOCKUP — panels b/c/d use real V12/V13 data (simplified time-weighted-mean calculation, not the locked rank-based primary analysis). "
         "Panels a/e/f/g are placeholders. Per the 2026-10-14 scope-of-disclosure decision, no cohorts other than V12, V13, and the new cohort appear anywhere on this page.",
         fontsize=7, color="#555555", wrap=True)

plt.savefig("/home/user/gd-cbd/figures/mockups/fig4_composite.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig4_composite.png")
