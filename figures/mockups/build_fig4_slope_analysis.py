"""
Figure 4g, revised: per-animal recovery slope via linear regression (not a
two-point baseline-to-72h difference), plus a sensitivity check across
candidate endpoints. Real per-animal data, same pooled V12+V13 cohort as
build_fig4.py / build_fig4g_slope.py (data/raw/prism_exports_2026-10-14/).

Why: a baseline->single-timepoint slope is driven entirely by whatever
noise sits at that one point (demonstrated directly on the 2026-11-03
run: one GD-CBD animal's 73.5h reading of 259.855, sandwiched between
128.225 at 48.5h and 63.320 at 100h, produced a slope of +3.2 %/h that
was really just that one point). A regression slope across each animal's
early timepoints (baseline plus every post-op reading up to ~72h) uses
the whole trajectory instead of one point.
"""
import numpy as np
import matplotlib.pyplot as plt

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
EARLY_CUTOFF = 75.0  # includes the ~72h point (73.5h V12, 68h V13), excludes later timepoints


def pct_series_with_baseline(baselines, hours, values):
    """Returns per-animal (hours incl. t=0, pct incl. 100 at t=0)."""
    out = []
    for b, series in zip(baselines, values):
        h = [0.0] + list(hours)
        p = [100.0] + [100.0 * v / b for v in series]
        out.append((np.array(h), np.array(p)))
    return out


def regression_slope(h, p, cutoff):
    mask = h <= cutoff
    if mask.sum() < 2:
        return np.nan
    slope, _ = np.polyfit(h[mask], p[mask], 1)
    return slope


# ---------- Panel A: regression slope per animal, 0 -> ~72h ----------
pooled_slope = {"Vehicle": [], "CBD": [], "GD-CBD": []}
for cohort in COHORT_ORDER:
    arms = DATA[cohort]
    for arm in ARM_ORDER:
        if arm not in arms:
            continue
        baselines, hours, values = arms[arm]
        for h, p in pct_series_with_baseline(baselines, hours, values):
            pooled_slope[arm].append(regression_slope(h, p, EARLY_CUTOFF))

fig, ax = plt.subplots(figsize=(4, 4))
x_positions = {"Vehicle": 0, "CBD": 1, "GD-CBD": 2}
rng = np.random.default_rng(2)
for arm in ARM_ORDER:
    vals = pooled_slope[arm]
    if not vals:
        continue
    xs = x_positions[arm] + rng.uniform(-0.08, 0.08, size=len(vals))
    ax.scatter(xs, vals, color=COLOR[arm], s=40, zorder=3, edgecolor="white", linewidth=0.5)
    mean = np.mean(vals)
    sem = np.std(vals, ddof=1) / np.sqrt(len(vals)) if len(vals) > 1 else 0.0
    ax.hlines(mean, x_positions[arm] - 0.22, x_positions[arm] + 0.22, color=COLOR[arm], linewidth=2.5, zorder=2)
    ax.errorbar(x_positions[arm], mean, yerr=sem, color=COLOR[arm], capsize=3, linewidth=1.5, zorder=2)

ax.axhline(0, color="#bbbbbb", linewidth=0.8, linestyle=":")
ax.set_xticks([0, 1, 2])
ax.set_xticklabels([f"Vehicle\n(n={len(pooled_slope['Vehicle'])})",
                     f"Free CBD\n(n={len(pooled_slope['CBD'])})",
                     f"GD-CBD\n(n={len(pooled_slope['GD-CBD'])})"])
ax.set_ylabel("Regression slope, 0→~72h\n(% of baseline per hour)")
ax.set_title("Figure 4g (revised) — per-animal recovery slope\nlinear fit, all early timepoints, V12+V13 pooled",
             fontsize=9.5, fontweight="bold")
fig.text(0.01, -0.09,
         "REAL. Linear regression per animal across baseline (t=0, 100%) plus every post-op reading "
         "up to ~72h (5 points in V12, 5 in V13), not a two-point slope. Less sensitive to a single "
         "noisy timepoint than the baseline→one-endpoint version.",
         fontsize=7.3, color="#555555", wrap=True)
plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4g_regression_slope.png", dpi=200, bbox_inches="tight")
plt.close()

print("=== Regression slope (0 -> ~72h), per arm ===")
for arm in ARM_ORDER:
    vals = pooled_slope[arm]
    if vals:
        print(f"{arm}: n={len(vals)}, mean = {np.mean(vals):.4f} %/h, values = {[round(v, 3) for v in vals]}")

# ---------- Panel B: sensitivity -- two-point slope at every candidate endpoint ----------
# Use each cohort's own timepoint grid; align by rank order (1st post-op reading,
# 2nd, 3rd...) since V12 and V13 sampled on slightly different hours.
rank_labels = ["1st reading", "2nd", "3rd", "4th", "5th (~72h)", "6th", "7th", "8th", "9th"]
endpoint_hours_by_cohort = {c: DATA[c][ARM_ORDER[-1] if ARM_ORDER[-1] in DATA[c] else list(DATA[c])[0]][1]
                             for c in COHORT_ORDER}

slope_by_rank = {arm: [] for arm in ARM_ORDER}  # list of (mean_slope, sem) per rank
n_ranks = 9
for rank in range(n_ranks):
    for arm in ARM_ORDER:
        vals = []
        for cohort in COHORT_ORDER:
            arms = DATA[cohort]
            if arm not in arms:
                continue
            baselines, hours, values = arms[arm]
            t = hours[rank]
            for b, series in zip(baselines, values):
                pct = 100.0 * series[rank] / b
                vals.append((pct - 100.0) / t)
        if vals:
            slope_by_rank[arm].append((np.mean(vals), np.std(vals, ddof=1) / np.sqrt(len(vals)) if len(vals) > 1 else 0.0, len(vals)))
        else:
            slope_by_rank[arm].append((np.nan, np.nan, 0))

approx_hours = [np.mean([DATA[c][a][1][r] for c in COHORT_ORDER for a in ARM_ORDER if a in DATA[c]])
                for r in range(n_ranks)]

fig, ax = plt.subplots(figsize=(7, 4))
for arm in ARM_ORDER:
    means = [m for m, s, n in slope_by_rank[arm]]
    sems = [s for m, s, n in slope_by_rank[arm]]
    ax.errorbar(approx_hours, means, yerr=sems, color=COLOR[arm], marker="o", markersize=5,
                linewidth=1.8, capsize=3, label=arm)

ax.axhline(0, color="#bbbbbb", linewidth=0.8, linestyle=":")
ax.axvline(72, color="#d9a300", linewidth=1.2, linestyle="--", alpha=0.7)
ax.text(72, ax.get_ylim()[1] if ax.get_ylim()[1] > 0 else 0.5, " 72h", color="#d9a300", fontsize=8, va="bottom")
ax.set_xlabel("Endpoint used for the baseline→endpoint slope (h, approx., cohorts averaged by reading order)")
ax.set_ylabel("Mean two-point slope\n(% of baseline per hour)")
ax.set_title("Sensitivity: does the GD-CBD-faster-recovery pattern hold at every endpoint?",
             fontsize=10, fontweight="bold")
ax.legend(frameon=False, fontsize=9)
fig.text(0.01, -0.1,
         "REAL, same pooled V12+V13 data. Each point is the mean two-point slope (baseline→that "
         "timepoint) if that endpoint had been picked instead of ~72h. V12 and V13 sampled on slightly "
         "different hours; x position is the across-cohort average for that reading's rank order.",
         fontsize=7.3, color="#555555", wrap=True)
plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4g_sensitivity.png", dpi=200, bbox_inches="tight")
plt.close()

print("\n=== Sensitivity: mean two-point slope by endpoint rank ===")
for r in range(n_ranks):
    row = f"rank {r+1} (~{approx_hours[r]:.0f}h): "
    row += ", ".join(f"{arm}={slope_by_rank[arm][r][0]:.3f}" for arm in ARM_ORDER if not np.isnan(slope_by_rank[arm][r][0]))
    print(row)

print("\nSaved: fig4g_regression_slope.png, fig4g_sensitivity.png")
