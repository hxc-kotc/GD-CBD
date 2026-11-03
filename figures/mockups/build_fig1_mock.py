import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrow, FancyBboxPatch
from mock_helpers import watermark, status_tag, panel_letter, RNG

fig = plt.figure(figsize=(11, 8))
fig.suptitle("Figure 1 — Chemistry and characterization of GD-CBD (MOCKUP)", fontsize=14, fontweight="bold", x=0.02, ha="left", y=0.98)
gs = GridSpec(2, 2, figure=fig, hspace=0.5, wspace=0.35, top=0.89, bottom=0.17, left=0.08, right=0.95)

# 1a: synthesis scheme - REAL scheme (panel c of the chemist's own synthesis figure,
# cropped from the source image; the ketamine-conjugate panel (b) in that source figure
# is not ours and is excluded). Two real steps: CBD + azido-PEG4-COOH -> bifunctional
# PEG linker-CBD (in DMF); GD2-OH96 + propargyl bromide -> GD2-acetylene (4), then CuAAC
# click of (4) with the linker-CBD to give GD-CBD (7). Real route, so status is "Have",
# not "Box" - this is the one panel in this figure that isn't illustrative.
ax_a = fig.add_subplot(gs[0, 0])
img_a = mpimg.imread("/home/user/gd-cbd/literature/chemistry_scheme/panel_c_GD2-CBD_clean.png")
ax_a.imshow(img_a)
ax_a.axis("off")
ax_a.set_title("Synthesis scheme (real route)", fontsize=9)
panel_letter(ax_a, "a")
status_tag(ax_a, "Have")

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
ax_c.set_xticks(range(0, 169, 24))  # 24h chunks, consistent with the other long time-series panels
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

# Panel 1e (hemocompatibility/CARPA) cut 2026-11-03: never discussed at the 2026-11-02
# PI session, this repo's own anticipatory addition, and it sat oddly next to a paper
# that session settled firmly against making any safety claims for. Not cut on
# inference - the user confirmed the cut after an explicit ask.

fig.text(0.02, 0.01,
         "Figure 1. Synthesis and characterization of GD-CBD. (a) Synthesis scheme: CBD + azido-PEG4-COOH gives a bifunctional PEG linker-CBD; GD2 (OH96) + propargyl "
         "bromide gives GD2-acetylene; CuAAC click of the two gives GD-CBD. (b) Physicochemical characterization: size (DLS), zeta potential, CBD loading, HPLC purity, and "
         "molecular weight. (c) In vitro CBD release under lysosomal-mimetic (pH 5.5) vs. plasma-mimetic (pH 7.4) conditions. (d) Stacked 1H NMR traces for CBD, the linker "
         "intermediate, and GD-CBD. "
         "Panel a is the chemist's real synthesis scheme, not a mockup. Values in b/c/d are illustrative placeholders, not measurements. Panels b and c are scaled to "
         "Sharma 2024's GD2-VPA data (same GD platform, same CuAAC click linker chemistry: 4.4 nm, near-neutral zeta, 6 wt% loading, 99% purity, ~80% release by day 7 at "
         "pH 5.5 vs. <6% by day 7 at pH 7.4), not arbitrary numbers. Real data pending: Batch 4 identity (~Oct 23), release profile, spectra.",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig1_box_layout.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig1_box_layout.png (4 panels: a-d)")
