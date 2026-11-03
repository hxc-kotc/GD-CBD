"""
Figure 4g builder - per-animal slope, baseline to ~72h.
Real per-animal data, V12+V13 pooled (same source and transcription as
build_fig4.py: data/raw/prism_exports_2026-10-14/). New secondary readout
per the 2026-11-02 PI session, alongside the AUC primary (panel c).

Slope = (% of baseline at the ~72h timepoint - 100) / hours elapsed,
per animal. Baseline is 100% by definition at t=0 (it's what each
animal's raw thresholds are normalized against), so this is a two-point
slope: baseline -> nearest timepoint to 72h (73.5h for V12, 68h for V13).
Replaces the ALT/AST and open-field panels (g/h), cut 2026-11-03 - no
toxicity figure in this paper.
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

# Same per-animal raw thresholds as build_fig4.py (data/raw/prism_exports_2026-10-14/).
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
TARGET_HOUR = 72.0


def nearest_hour_index(hours, target):
    h = np.array(hours, dtype=float)
    return int(np.argmin(np.abs(h - target)))


def per_animal_slopes(baselines, hours, values, target=TARGET_HOUR):
    """slope (%/h) from baseline (100%, t=0) to the timepoint nearest `target`."""
    idx = nearest_hour_index(hours, target)
    t = hours[idx]
    out = []
    for b, series in zip(baselines, values):
        pct_t = 100.0 * series[idx] / b
        out.append((pct_t - 100.0) / t)
    return out, t


pooled = {"Vehicle": [], "CBD": [], "GD-CBD": []}
used_hours = {}
for cohort in COHORT_ORDER:
    arms = DATA[cohort]
    for arm in ARM_ORDER:
        if arm not in arms:
            continue
        baselines, hours, values = arms[arm]
        slopes, t_used = per_animal_slopes(baselines, hours, values)
        pooled[arm].extend(slopes)
        used_hours[(cohort, arm)] = t_used

fig, ax = plt.subplots(figsize=(4, 4))
x_positions = {"Vehicle": 0, "CBD": 1, "GD-CBD": 2}
rng = np.random.default_rng(0)
for arm in ARM_ORDER:
    vals = pooled[arm]
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
ax.set_xticklabels([f"Vehicle\n(n={len(pooled['Vehicle'])})",
                     f"Free CBD\n(n={len(pooled['CBD'])})",
                     f"GD-CBD\n(n={len(pooled['GD-CBD'])})"])
ax.set_ylabel("Slope, baseline to ~72h\n(% of baseline per hour)")
ax.set_title("Figure 4g — per-animal slope, baseline→~72h\nV12+V13 pooled (n=14)", fontsize=10, fontweight="bold")

fig.text(0.01, -0.08,
         "REAL — computed from the same pooled V12+V13 per-animal data as panels b/c. "
         "Two-point slope: baseline (100%, t=0) to the timepoint nearest 72h "
         "(73.5h in V12, 68h in V13). Prespecified secondary readout; AUC (panel c) stays primary.",
         fontsize=7.5, color="#555555", wrap=True)
plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.savefig("/home/user/gd-cbd/figures/mockups/fig4g_slope.png", dpi=200, bbox_inches="tight")
plt.close()

print("Timepoints used for the ~72h slope:", used_hours)
for arm in ARM_ORDER:
    vals = pooled[arm]
    if vals:
        print(f"{arm}: n={len(vals)}, mean slope = {np.mean(vals):.4f} %/h, values = {[round(v, 3) for v in vals]}")
print("Saved: fig4g_slope.png")
