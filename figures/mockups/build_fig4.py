"""
Figure 4 mockup builder - GD-CBD flank-incision efficacy.
Real per-animal data from the two published discovery cohorts (V12, V13),
transcribed and verified from source files read this session
(data/raw/prism_exports_2026-10-14/). This is a MOCKUP for the Friday
presentation, not the locked final analysis.

Per the user's decision (2026-10-14): only V12 and V13 appear in the
manuscript. Other historical cohorts (V16/V18/V20/V21/V22/V23/V24) are
internal lab record only (data/raw/, cohort_identity_notes) and do not
appear in any figure or table that feeds the paper.

House color convention matches the lab's own existing slide ("Standard (g),
Avg & SEM"): GD-CBD = green, free CBD = gray, vehicle/operated control = black.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

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
    out = []
    for b, series in zip(baselines, values):
        out.append([100.0 * v / b for v in series])
    return out


def time_weighted_mean_pct(hours, pct_series):
    h = np.array(hours, dtype=float)
    out = []
    for series in pct_series:
        y = np.array(series, dtype=float)
        auc = np.trapezoid(y, h)
        out.append(auc / (h[-1] - h[0]))
    return out


# ========== Panel 4b: time course, percent of baseline, V12 / V13 only ==========
fig, axes = plt.subplots(1, 2, figsize=(8, 3.4), sharey=True)
fig.suptitle("Figure 4b (MOCKUP) — 50% withdrawal threshold, percent of baseline",
             fontsize=11, fontweight="bold", x=0.01, ha="left")

for ax, cohort in zip(axes, COHORT_ORDER):
    arms = DATA[cohort]
    for arm in ARM_ORDER:
        if arm not in arms:
            continue
        baselines, hours, values = arms[arm]
        pct = pct_baseline(baselines, values)
        pct_arr = np.array(pct)
        mean = pct_arr.mean(axis=0)
        sem = pct_arr.std(axis=0, ddof=1) / np.sqrt(pct_arr.shape[0]) if pct_arr.shape[0] > 1 else np.zeros_like(mean)
        ax.errorbar(hours, mean, yerr=sem, color=COLOR[arm], marker="o", markersize=4,
                     linewidth=1.8, capsize=3, label=arm)
    ax.axhline(100, color="#bbbbbb", linewidth=0.8, linestyle=":")
    ax.set_title(cohort, fontsize=10)
    ax.set_xlabel("Hours")
    ax.set_ylim(0, 350)

axes[0].set_ylabel("% of baseline threshold")
handles = [Line2D([0], [0], color=COLOR[a], marker="o", markersize=5, label=a) for a in ARM_ORDER]
fig.legend(handles=handles, loc="upper right", ncol=3, frameon=False, fontsize=9, bbox_to_anchor=(0.99, 1.1))
fig.text(0.01, -0.06,
         "MOCKUP — illustrative, not the locked primary analysis. The two discovery cohorts (same early preparation). "
         "New cohort (independent preparation, Nov 2026) overlays here once unblinded.",
         fontsize=7.5, color="#555555", wrap=True)
plt.tight_layout(rect=[0, 0.05, 1, 0.88])
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4b_timecourse.png", dpi=200, bbox_inches="tight")
plt.close()

# ========== Panel 4c: AUC, individual animals, V12+V13 pooled ==========
fig, ax = plt.subplots(figsize=(4, 4))
pooled_vals = {"Vehicle": [], "CBD": [], "GD-CBD": []}
for cohort in COHORT_ORDER:
    arms = DATA[cohort]
    for arm in ARM_ORDER:
        if arm not in arms:
            continue
        baselines, hours, values = arms[arm]
        pct = pct_baseline(baselines, values)
        pooled_vals[arm].extend(time_weighted_mean_pct(hours, pct))

x_positions = {"Vehicle": 0, "CBD": 1, "GD-CBD": 2}
rng = np.random.default_rng(0)
for arm in ARM_ORDER:
    vals = pooled_vals[arm]
    if not vals:
        continue
    xs = x_positions[arm] + rng.uniform(-0.08, 0.08, size=len(vals))
    ax.scatter(xs, vals, color=COLOR[arm], s=40, zorder=3, edgecolor="white", linewidth=0.5)
    mean = np.mean(vals)
    ax.hlines(mean, x_positions[arm] - 0.22, x_positions[arm] + 0.22, color=COLOR[arm], linewidth=2.5, zorder=2)

ax.set_xticks([0, 1, 2])
ax.set_xticklabels([f"Vehicle\n(n={len(pooled_vals['Vehicle'])})",
                     f"Free CBD\n(n={len(pooled_vals['CBD'])})",
                     f"GD-CBD\n(n={len(pooled_vals['GD-CBD'])})"])
ax.set_ylabel("Time-weighted mean, % of baseline\n(post-surgery window)")
ax.set_title("Figure 4c (MOCKUP)\nV12+V13 — the discovery dataset", fontsize=10, fontweight="bold")
ax.set_ylim(0, max(max(v) for v in pooled_vals.values() if v) * 1.15)
plt.tight_layout()
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4c_auc_pooled.png", dpi=200, bbox_inches="tight")
plt.close()

# ========== Panel 4d: per-cohort effect, V12, V13, and a pending slot for the new cohort ==========
fig, ax = plt.subplots(figsize=(6.5, 2.4))
rows = []
for cohort in COHORT_ORDER:
    arms = DATA[cohort]
    b_gd, h_gd, v_gd = arms["GD-CBD"]
    b_ve, h_ve, v_ve = arms["Vehicle"]
    gd_vals = time_weighted_mean_pct(h_gd, pct_baseline(b_gd, v_gd))
    ve_vals = time_weighted_mean_pct(h_ve, pct_baseline(b_ve, v_ve))
    diff = np.mean(gd_vals) - np.mean(ve_vals)
    se = np.sqrt(np.var(gd_vals, ddof=1) / len(gd_vals) + np.var(ve_vals, ddof=1) / len(ve_vals))
    rows.append((cohort, diff, se, len(gd_vals), len(ve_vals)))

rows = rows[::-1]
y = np.arange(len(rows) + 1)  # +1 for the pending new-cohort row
diffs = [r[1] for r in rows]
ses = [r[2] for r in rows]
labels = [f"{r[0]}  (GD-CBD n={r[3]}, veh n={r[4]})" for r in rows]

ax.errorbar(diffs, y[1:], xerr=[1.96 * s for s in ses], fmt="D", color="#2E7D32",
            markersize=7, capsize=3, linewidth=1.8, ecolor="#555555")
# pending row
ax.scatter([0], [0], marker="s", s=120, facecolor="#f2f2f2", edgecolor="#9E9E9E", linewidth=1.2, zorder=3)
ax.text(0, 0, "?", ha="center", va="center", fontsize=9, color="#9E9E9E", fontweight="bold")

ax.axvline(0, color="#999999", linewidth=1, linestyle="--")
ax.set_yticks(list(y))
ax.set_yticklabels(["New cohort (Nov 2026) — pending"] + labels)
ax.set_xlabel("GD-CBD minus vehicle, time-weighted mean % of baseline (illustrative, ~95% CI)")
ax.set_title("Figure 4d (MOCKUP) — per-cohort effect", fontsize=10, fontweight="bold")
fig.text(0.01, -0.1,
         "MOCKUP — simplified mean-difference, not the locked rank-based primary analysis. "
         "Shows only the two published discovery cohorts plus the pending new cohort.",
         fontsize=7.5, color="#555555")
plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4d_forest.png", dpi=200, bbox_inches="tight")
plt.close()

print("Saved: fig4b_timecourse.png, fig4c_auc_pooled.png, fig4d_forest.png (V12/V13 only)")
