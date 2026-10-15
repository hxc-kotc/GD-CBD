import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrow, FancyBboxPatch
from mock_helpers import watermark, status_tag, panel_letter, RNG

fig = plt.figure(figsize=(11, 8))
fig.suptitle("Figure 1 — Chemistry and characterization of GD-CBD (MOCKUP)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.98)
gs = GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.35, top=0.91, bottom=0.14, left=0.08, right=0.95, height_ratios=[1, 1, 0.75])

# 1a: synthesis scheme - schematic diagram, not mock data (no numbers to fake)
ax_a = fig.add_subplot(gs[0, 0])
ax_a.set_xlim(0, 8.4); ax_a.set_ylim(0.25, 3.15); ax_a.axis("off")
boxes = [("GD", 0.8), ("GD-linker", 3.6), ("CBD-azide", 3.6), ("GD-CBD", 7.2)]
ys = [2.6, 2.6, 0.8, 1.7]
labels_xy = [(0.8, 2.6), (3.6, 2.6), (3.6, 0.8), (7.2, 1.7)]
for (label, x), y in zip([("GD", 0.8), ("GD-linker", 3.6), ("CBD-N3", 3.6), ("GD-CBD", 7.2)], [2.6, 2.6, 0.8, 1.7]):
    ax_a.add_patch(FancyBboxPatch((x - 0.7, y - 0.35), 1.6, 0.7, boxstyle="round,pad=0.02", edgecolor="#2E7D32", facecolor="#E8F5E9", linewidth=1.3))
    ax_a.text(x + 0.1, y, label, ha="center", va="center", fontsize=8, fontweight="bold")
ax_a.annotate("", xy=(2.9, 2.6), xytext=(1.5, 2.6), arrowprops=dict(arrowstyle="->", color="#555555"))
ax_a.text(2.2, 2.85, "linker", fontsize=6.5, ha="center", color="#555555")
ax_a.annotate("", xy=(6.5, 1.9), xytext=(4.3, 2.4), arrowprops=dict(arrowstyle="->", color="#555555"))
ax_a.annotate("", xy=(6.5, 1.5), xytext=(4.3, 1.0), arrowprops=dict(arrowstyle="->", color="#555555"))
ax_a.text(5.4, 2.0, "CuAAC click", fontsize=6.5, ha="center", color="#555555")
ax_a.set_title("Synthesis scheme (schematic, route TBD by chemist)", fontsize=9)
panel_letter(ax_a, "a")
status_tag(ax_a, "Box")

# 1b: physicochemical table - mock values, calibrated to Sharma 2024 (GD2-VPA): same GD
# platform and same CuAAC click linker chemistry as GD-CBD. GD2 itself: 4.4 nm, nearly
# neutral zeta. GD2-VPA: 6 wt% loading (7-8 drug molecules/dendrimer), 99% HPLC purity.
ax_b = fig.add_subplot(gs[0, 1])
ax_b.axis("off")
rows = [("Size (DLS)", "~4.5 ± 0.5 nm"), ("Zeta potential", "~0 to +2 mV (near neutral)"),
        ("CBD loading (NMR)", "~6-8% w/w"), ("HPLC purity", "~99%"), ("MW", "~X kDa (TBD)")]
tbl = ax_b.table(cellText=rows, colLabels=["Property", "Value (mock)"], loc="center", cellLoc="left")
tbl.auto_set_font_size(False); tbl.set_fontsize(8); tbl.scale(1, 1.6)
for (r, c), cell in tbl.get_celld().items():
    cell.set_edgecolor("#cccccc")
    if r == 0:
        cell.set_facecolor("#E3E8F0"); cell.set_text_props(fontweight="bold")
watermark(ax_b, "MOCK")
ax_b.set_title("Physicochemical characterization", fontsize=9, y=1.05)
panel_letter(ax_b, "b")
status_tag(ax_b, "Box")

# 1c: release profile - mock two curves, shaped to match Sharma 2024's GD2-VPA release data
# (same enzyme-cleavable linker + CuAAC chemistry as GD-CBD): ~80% release by day 7 (168h)
# under esterase/pH 5.5 (lysosomal-mimetic); <6% by day 7, minimal release up to 48h, under
# PBS/pH 7.4 (plasma-mimetic) - not a generic release shape, these are that paper's own numbers.
t = np.linspace(0, 168, 60)
ax_c = fig.add_subplot(gs[1, 0])
lyso = 80 / (1 + np.exp(-(t - 55) / 22)) + RNG.normal(0, 2, len(t))
plasma = 5.5 * (1 - np.exp(-t / 130)) + RNG.normal(0, 0.4, len(t))
ax_c.plot(t, lyso, color="#2E7D32", linewidth=1.8, label="Lysosomal (pH 5.5)")
ax_c.plot(t, plasma, color="#757575", linewidth=1.8, label="Plasma (pH 7.4)")
ax_c.set_xlabel("Hours", fontsize=8); ax_c.set_ylabel("% CBD released", fontsize=8)
ax_c.legend(fontsize=7, frameon=False)
watermark(ax_c)
ax_c.set_title("Release profile", fontsize=9)
panel_letter(ax_c, "c")
status_tag(ax_c, "Box")

# 1d: stacked NMR traces - mock
ax_d = fig.add_subplot(gs[1, 1])
x = np.linspace(0, 10, 500)
def spectrum(peaks, offset):
    y = np.zeros_like(x)
    for p, h in peaks:
        y += h * np.exp(-((x - p) ** 2) / (2 * 0.04 ** 2))
    return y + offset
ax_d.plot(x, spectrum([(1.2, 1), (3.4, 0.6), (7.2, 0.8)], 0), color="#111111", linewidth=0.8)
ax_d.plot(x, spectrum([(1.2, 1), (3.4, 0.6), (4.1, 0.5)], 2.5), color="#757575", linewidth=0.8)
ax_d.plot(x, spectrum([(1.2, 1), (3.4, 0.6), (4.1, 0.5), (7.8, 0.4)], 5), color="#2E7D32", linewidth=0.8)
ax_d.text(9.7, 0.3, "CBD", fontsize=7, ha="right"); ax_d.text(9.7, 2.8, "intermediate", fontsize=7, ha="right")
ax_d.text(9.7, 5.3, "GD-CBD", fontsize=7, ha="right")
ax_d.invert_xaxis(); ax_d.set_yticks([]); ax_d.set_xlabel("δ (ppm)", fontsize=8)
watermark(ax_d)
ax_d.set_title("¹H NMR, stacked traces", fontsize=9)
panel_letter(ax_d, "d")
status_tag(ax_d, "Box")

# 1e: hemocompatibility / complement activation - mock. No comparator paper runs this
# assay (checked: none of the four report hemolysis/complement/CARPA data), so these
# values are NOT calibrated to a specific paper - they're set in line with the published
# hydroxyl-PAMAM/glucose-dendrimer biocompatibility literature generally (hydroxyl-terminated
# dendrimers are consistently reported as non-hemolytic, well below the <5% hemolysis /
# <2-fold complement-activation thresholds used to call a nanomaterial "safe" in that
# literature) - unlike amine-terminated dendrimers, which are not. All three assays plotted
# as fold-vs-baseline so they share one y-axis; dotted line marks a common "flag for
# follow-up" convention (2x baseline), not a true normal-range ceiling like panel 4g's.
ax_e = fig.add_subplot(gs[2, :])
assays = ["Hemolysis\n(fold vs. PBS control)", "C3a\n(fold vs. baseline)", "Platelet activation\n(fold vs. baseline)"]
gd_alone = [1.1, 1.1, 1.05]
gd_cbd = [1.2, 1.15, 1.1]
gd_alone_err = [0.15, 0.15, 0.1]
gd_cbd_err = [0.2, 0.2, 0.15]
xpos = np.arange(3)
w = 0.32
ax_e.axhline(2.0, color="#D32F2F", linewidth=0.8, linestyle=":")
ax_e.text(2.35, 2.05, "flag for follow-up (2x)", fontsize=6.5, color="#D32F2F", va="bottom")
ax_e.bar(xpos - w / 2, gd_alone, width=w, yerr=gd_alone_err, color="#5B8DB8", capsize=3, label="GD alone", edgecolor="white")
ax_e.bar(xpos + w / 2, gd_cbd, width=w, yerr=gd_cbd_err, color="#2E7D32", capsize=3, label="GD-CBD", edgecolor="white")
ax_e.set_xticks(xpos); ax_e.set_xticklabels(assays, fontsize=7.5)
ax_e.set_ylim(0, 2.6)
ax_e.set_ylabel("Fold vs. negative control", fontsize=8)
ax_e.legend(fontsize=7.5, frameon=False, loc="upper left")
watermark(ax_e, "MOCK")
ax_e.set_title("Hemocompatibility and complement activation (CARPA panel)", fontsize=9)
panel_letter(ax_e, "e")
status_tag(ax_e, "Box")

fig.text(0.02, 0.01,
         "Figure 1. Synthesis and characterization of GD-CBD. (a) Synthesis scheme: GD core to GD-linker intermediate to GD-CBD via CuAAC click conjugation with CBD-N3. "
         "(b) Physicochemical characterization: size (DLS), zeta potential, CBD loading, HPLC purity, and molecular weight. (c) In vitro CBD release under lysosomal-mimetic "
         "(pH 5.5) vs. plasma-mimetic (pH 7.4) conditions. (d) Stacked 1H NMR traces for CBD, the linker intermediate, and GD-CBD. (e) Hemolysis, complement activation (C3a), "
         "and platelet activation, GD alone vs. GD-CBD, anticipating a standard nanomedicine preclinical question not otherwise in this plan. "
         "Panel a reflects the real synthesis route; values in b/c/d/e are illustrative placeholders, not measurements. Panels b and c are scaled to Sharma 2024's GD2-VPA data "
         "(same GD platform, same CuAAC click linker chemistry: 4.4 nm, near-neutral zeta, 6 wt% loading, 99% purity, ~80% release by day 7 at pH 5.5 vs. <6% by day 7 at pH 7.4), "
         "not arbitrary numbers. Panel e has no comparator-paper precedent (none of the four run this assay) — scaled instead to published hydroxyl-dendrimer biocompatibility "
         "ranges. Real data pending: Batch 4 identity (~Oct 23), release profile, spectra; panel e is not yet a planned assay — included to show the shape if added.",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig1_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig1_box_layout.png (5 panels: a-e)")
