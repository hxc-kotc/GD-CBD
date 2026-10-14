"""
Figure 4 mockup builder - GD-CBD flank-incision efficacy.
Real historical per-animal data, transcribed directly from source files read
and verified in this session (data/raw/prism_exports_2026-10-14/). This is a
MOCKUP for the Friday presentation, not the locked final analysis - the
primary-endpoint script (AUC 24-168h, % of baseline) is written here in
simplified form for illustration.

House color convention matches the lab's own existing slide ("Standard (g),
Avg & SEM"): GD-CBD = green, free CBD = gray, vehicle/operated control = black.
Cohorts distinguished by marker/linestyle, never by a new hue (fixed categorical
assignment per dataviz skill: color encodes ARM, not cohort).
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

# ---- per-animal data: {cohort: {arm: (baseline_list, hours, [animal_value_lists])}} ----
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
    "V20 (Jul 2025)": {
        "GD-CBD": ([81, 34, 30],
                   [2, 4, 6, 23.5, 48, 71, 95.5, 118.5, 143.5, 167.5],
                   [[61.085, 17.450, 22.600, 15.100, 166.600, 9.800, 25.700, 10.500, 5.005, 18.850],
                    [7.420, 4.080, 4.600, 3.600, 23.100, 10.900, 3.300, 3.800, 2.875, 2.855],
                    [11.045, 4.170, 83.200, 9.100, 6.500, 14.900, 17.100, 6.500, 5.510, 5.045]]),
        "CBD": ([48, 78, 33],
                [2, 4, 6, 23.5, 48, 71, 95.5, 118.5, 143.5, 167.5],
                [[12.355, 3.025, 4.200, 3.200, 15.200, 4.500, 2.100, 3.700, 3.345, 1.630],
                 [4.785, 6.300, 4.700, 9.800, 12.000, 5.700, 13.300, 10.000, 9.725, 4.520],
                 [14.240, 4.315, 240.100, 28.700, 22.400, 3.600, 3.800, 5.800, 3.235, 3.965]]),
        "Vehicle": ([99, 82],
                    [2, 4, 6, 23.5, 48, 71, 95.5, 118.5, 143.5, 167.5],
                    [[233.840, 64.910, 75.500, 72.700, 65.500, 82.900, 76.600, 20.300, 9.745, 23.895],
                     [8.700, 6.750, 7.100, 20.300, 7.900, 7.600, 3.200, 11.700, 8.795, 7.420]]),
    },
    "V22 72h-only (Sept 2025)": {
        "GD-CBD": ([41.7, 42.4, 51.5],
                   [2, 4, 6, 24, 48.5, 70.5],
                   [[17.6, 29.7, 21.5, 32.9, 9.3, 5.7],
                    [5.3, 9.3, 3.2, 5.0, 6.0, 7.5],
                    [15.7, 7.9, 7.4, 8.0, 14.2, 9.8]]),
        "CBD": ([32.8, 33.2, 97.8],
                [2, 4, 6, 24, 48.5, 70.5],
                [[42.2, 11.7, 14.2, 13.1, 7.3, 7.1],
                 [3.5, 4.3, 5.0, 2.4, 4.1, 5.4],
                 [271.0, 137.7, 36.5, 45.7, 9.8, 21.9]]),
        "Vehicle": ([50.8, 49.2],
                    [2, 4, 6, 24, 48.5, 70.5],
                    [[5.8, 3.7, 8.3, 3.9, 25.8, 4.4],
                     [19.2, 49.9, 22.5, 24.9, 17.5, 14.2]]),
    },
    "V23 (Apr 2026)": {
        "GD-CBD": ([6.2, 21.5, 16.4],
                   [2, 4, 6, 26, 50, 74, 96, 123, 152, 171.5],
                   [[3.4, 3.9, 7.6, 6.5, 11.2, 3.0, 4.7, 1.3, 3.4, 2.6],
                    [6.3, 15.9, 8.0, 16.1, 5.5, 8.2, 11.9, 9.5, 5.6, 3.3],
                    [12.5, 6.8, 12.7, 67.0, 6.5, 22.1, 7.0, 4.9, 10.3, 6.1]]),
        "Vehicle": ([35.8, 9.5],
                    [2, 4, 6, 26, 50, 74, 96, 123, 152, 171.5],
                    [[23.0, 25.0, 39.4, 29.2, 83.2, 43.1, 41.5, 40.0, 14.2, 26.6],
                     [23.3, 13.2, 10.0, 28.0, 10.1, 26.7, 8.7, 9.4, 6.8, 5.0]]),
    },
}

ARM_ORDER = ["Vehicle", "CBD", "GD-CBD"]
COHORT_ORDER = list(DATA.keys())


def pct_baseline(baselines, values):
    """values: list of per-animal lists -> list of per-animal %-of-baseline lists."""
    out = []
    for b, series in zip(baselines, values):
        out.append([100.0 * v / b for v in series])
    return out


def time_weighted_mean_pct(hours, pct_series):
    """Per animal: trapezoidal mean of %-of-baseline over its own observed window."""
    h = np.array(hours, dtype=float)
    out = []
    for series in pct_series:
        y = np.array(series, dtype=float)
        auc = np.trapezoid(y, h)
        out.append(auc / (h[-1] - h[0]))
    return out


# ========== Panel 4b: time course, percent of baseline, small multiples by cohort ==========
fig, axes = plt.subplots(1, 5, figsize=(16, 3.2), sharey=True)
fig.suptitle("Figure 4b (MOCKUP) — 50% withdrawal threshold, percent of baseline, by cohort",
             fontsize=11, fontweight="bold", x=0.01, ha="left")

for ax, cohort in zip(axes, COHORT_ORDER):
    arms = DATA[cohort]
    for arm in ARM_ORDER:
        if arm not in arms:
            continue
        baselines, hours, values = arms[arm]
        pct = pct_baseline(baselines, values)
        pct_arr = np.array(pct)  # n_animals x n_timepoints
        mean = pct_arr.mean(axis=0)
        sem = pct_arr.std(axis=0, ddof=1) / np.sqrt(pct_arr.shape[0]) if pct_arr.shape[0] > 1 else np.zeros_like(mean)
        ax.errorbar(hours, mean, yerr=sem, color=COLOR[arm], marker="o", markersize=3,
                     linewidth=1.5, capsize=2, label=arm)
    ax.axhline(100, color="#bbbbbb", linewidth=0.8, linestyle=":")
    ax.set_title(cohort, fontsize=8.5)
    ax.set_xlabel("Hours")
    ax.set_ylim(0, 350)

axes[0].set_ylabel("% of baseline threshold")
handles = [Line2D([0], [0], color=COLOR[a], marker="o", markersize=4, label=a) for a in ARM_ORDER]
fig.legend(handles=handles, loc="upper right", ncol=3, frameon=False, fontsize=9, bbox_to_anchor=(0.99, 1.08))
fig.text(0.01, -0.04,
         "MOCKUP — illustrative only, not the locked primary analysis. Baselines differ ~3-17x across cohorts (already flagged as a limitation); "
         "plotting percent-of-baseline rather than raw grams here so cohorts are visually comparable. V22 truncated at 70.5h (not a full 168h window). "
         "n=2 per vehicle/control arm in every cohort shown.",
         fontsize=7, color="#555555", wrap=True)
plt.tight_layout(rect=[0, 0.02, 1, 0.93])
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4b_timecourse.png", dpi=200, bbox_inches="tight")
plt.close()

# ========== Panel 4c: AUC (time-weighted mean %-of-baseline), individual animals, pooled V12+V13 ==========
fig, ax = plt.subplots(figsize=(4, 4))
pooled_vals = {"Vehicle": [], "CBD": [], "GD-CBD": []}
for cohort in ["V12 (Dec 2024)", "V13 (Jan 2025)"]:
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
ax.set_xticklabels(["Vehicle\n(n=4)", "Free CBD\n(n=3)", "GD-CBD\n(n=6)"])
ax.set_ylabel("Time-weighted mean, % of baseline\n(post-surgery window)")
ax.set_title("Figure 4c (MOCKUP)\nV12+V13 pooled — the discovery dataset", fontsize=10, fontweight="bold")
ax.set_ylim(0, max(max(v) for v in pooled_vals.values() if v) * 1.15)
plt.tight_layout()
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4c_auc_pooled.png", dpi=200, bbox_inches="tight")
plt.close()

# ========== Panel 4d: forest plot, per-cohort GD-CBD vs vehicle effect ==========
fig, ax = plt.subplots(figsize=(6.5, 3.2))
rows = []
for cohort in COHORT_ORDER:
    arms = DATA[cohort]
    if "GD-CBD" not in arms or "Vehicle" not in arms:
        continue
    b_gd, h_gd, v_gd = arms["GD-CBD"]
    b_ve, h_ve, v_ve = arms["Vehicle"]
    gd_vals = time_weighted_mean_pct(h_gd, pct_baseline(b_gd, v_gd))
    ve_vals = time_weighted_mean_pct(h_ve, pct_baseline(b_ve, v_ve))
    diff = np.mean(gd_vals) - np.mean(ve_vals)
    # rough pooled SE for illustration only
    se = np.sqrt(np.var(gd_vals, ddof=1) / len(gd_vals) + np.var(ve_vals, ddof=1) / len(ve_vals)) if len(gd_vals) > 1 and len(ve_vals) > 1 else 0
    rows.append((cohort, diff, se, len(gd_vals), len(ve_vals)))

rows = rows[::-1]  # plot top-to-bottom in chronological order
y = np.arange(len(rows))
diffs = [r[1] for r in rows]
ses = [r[2] for r in rows]
labels = [f"{r[0]}  (GD-CBD n={r[3]}, veh n={r[4]})" for r in rows]

ax.errorbar(diffs, y, xerr=[1.96 * s for s in ses], fmt="D", color="#2E7D32",
            markersize=6, capsize=3, linewidth=1.5, ecolor="#555555")
ax.axvline(0, color="#999999", linewidth=1, linestyle="--")
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=8)
ax.set_xlabel("GD-CBD minus vehicle, time-weighted mean % of baseline (illustrative, ~95% CI)")
ax.set_title("Figure 4d (MOCKUP) — per-cohort effect, replication across the historical record",
              fontsize=10, fontweight="bold")
fig.text(0.01, -0.06,
         "MOCKUP — simplified mean-difference, not the locked rank-based primary analysis. "
         "New cohort (Oct-Nov 2026) adds one more row here once unblinded. "
         "V22 row uses a 70.5h window only, not comparable in absolute scale to the others.",
         fontsize=7, color="#555555")
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4d_forest.png", dpi=200, bbox_inches="tight")
plt.close()

print("Saved: fig4b_timecourse.png, fig4c_auc_pooled.png, fig4d_forest.png")
for cohort, diff, se, ngd, nve in [ (r[0],r[1],r[2],r[3],r[4]) for r in rows ]:
    print(f"{cohort}: GD-CBD-vehicle diff = {diff:.1f} pct-of-baseline, n_gd={ngd}, n_veh={nve}")
