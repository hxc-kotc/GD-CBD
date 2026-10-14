import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrow, FancyBboxPatch
from mock_helpers import watermark, status_tag, panel_letter, RNG

fig = plt.figure(figsize=(11, 8))
fig.suptitle("Figure 1 — Chemistry and characterization of GD-CBD (MOCKUP)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.98)
gs = GridSpec(2, 2, figure=fig, hspace=0.5, wspace=0.35, top=0.89, bottom=0.08, left=0.08, right=0.95)

# 1a: synthesis scheme - schematic diagram, not mock data (no numbers to fake)
ax_a = fig.add_subplot(gs[0, 0])
ax_a.set_xlim(0, 10); ax_a.set_ylim(0, 4); ax_a.axis("off")
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

# 1b: physicochemical table - mock values
ax_b = fig.add_subplot(gs[0, 1])
ax_b.axis("off")
rows = [("Size (DLS)", "~6.0 ± 0.8 nm"), ("Zeta potential", "~−1 to 0 mV"),
        ("CBD loading (NMR)", "~X% w/w"), ("HPLC purity", "~X%"), ("MW", "~X kDa")]
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

# 1c: release profile - mock two curves
ax_c = fig.add_subplot(gs[1, 0])
t = np.linspace(0, 170, 60)
lyso = 85 / (1 + np.exp(-(t - 50) / 20)) + RNG.normal(0, 2, len(t))
plasma = 6 * (1 - np.exp(-t / 120)) + RNG.normal(0, 0.5, len(t))
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

fig.text(0.02, 0.01,
         "MOCKUP — panel a is a schematic (no numeric data to fake). Panels b/c/d show synthetic, illustrative values only — not real measurements. "
         "Real data pending: Batch 4 identity (~Oct 23), release profile, spectra.",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig1_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig1_box_layout.png")
