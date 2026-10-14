"""
Box-placeholder layout mockups for Figures 1, 2, 3 (epilepsy), 5, and the
conditional biodistribution figure. Literal labeled rectangles, status badges
(Have / Partial / Box), so Friday's audience sees the full shape of the paper
even where no data exists yet.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams.update({"font.family": "DejaVu Sans"})

STATUS_COLOR = {"Have": "#2E7D32", "Partial": "#B8860B", "Box": "#9E9E9E"}
STATUS_FACE = {"Have": "#E8F5E9", "Partial": "#FFF8E1", "Box": "#F2F2F2"}


def panel_grid(title, panels, filename, ncols=2, figsize=None, suptitle_note=None):
    """panels: list of (label, description, status, colspan)"""
    nrows = sum(1 for p in panels) // ncols + 1
    # simple vertical stack with colspan support, one row per panel group
    rows = []
    i = 0
    while i < len(panels):
        label, desc, status, colspan = panels[i]
        rows.append([(label, desc, status, colspan)])
        i += 1
    fig_h = 1.1 * len(rows) + 1
    fig, ax = plt.subplots(figsize=figsize or (9, fig_h))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, len(rows))
    ax.axis("off")
    ax.set_title(title, fontsize=13, fontweight="bold", loc="left", pad=14)

    for r, row in enumerate(rows):
        y = len(rows) - r - 1
        x = 0
        for label, desc, status, colspan in row:
            w = colspan
            rect = patches.FancyBboxPatch((x + 0.01, y + 0.06), w - 0.02, 0.88,
                                           boxstyle="round,pad=0.01,rounding_size=0.02",
                                           linewidth=1.4, edgecolor=STATUS_COLOR[status],
                                           facecolor=STATUS_FACE[status])
            ax.add_patch(rect)
            ax.text(x + 0.02, y + 0.72, label, fontsize=11, fontweight="bold", va="top")
            ax.text(x + 0.02, y + 0.50, desc, fontsize=8.5, va="top", wrap=True,
                    color="#333333")
            ax.text(x + w - 0.03, y + 0.16, status, fontsize=8.5, fontweight="bold",
                    ha="right", color=STATUS_COLOR[status])
            x += w
    if suptitle_note:
        fig.text(0.01, 0.01, suptitle_note, fontsize=7.5, color="#555555", wrap=True)
    plt.tight_layout(rect=[0, 0.03 if suptitle_note else 0, 1, 1])
    plt.savefig(f"/home/user/gd-cbd/figures/mockups/{filename}", dpi=200, bbox_inches="tight")
    plt.close()


panel_grid(
    "Figure 1 — Chemistry and characterization of GD-CBD",
    [
        ("1a", "Synthesis scheme (GD -> linker -> CBD, click chemistry)", "Box", 1),
        ("1b", "Physicochemical table: size, zeta, loading %, purity, MW", "Box", 1),
        ("1c", "Release profile: lysosomal (pH 5.5) vs plasma (pH 7.4), inset zoom\n[template: Sharma 2024 Fig. 10c]", "Box", 1),
        ("1d", "Representative NMR / HPLC / MALDI spectra\n[template: Sharma 2024 Fig. 10a-b]", "Box", 1),
    ],
    "fig1_box_layout.png",
    suptitle_note="All four panels await Batch 4 identity (chemist, due ~Oct 23) and release data (open item).",
)

panel_grid(
    "Figure 2 — In vitro activity",
    [
        ("2a", "TNF-a / cytokine panel: GD-CBD vs free CBD vs GD alone vs original batch, viability overlay", "Partial", 1),
        ("2b", "CB1 / CB2 binding or functional assay", "Box", 1),
        ("2c", "HU-331 stability-indicating chromatogram (supplement candidate)", "Box", 1),
    ],
    "fig2_box_layout.png",
    suptitle_note="2a: some prior TNF-a data exists; new-batch panel due ~Oct 23. 2b: open item, may not exist.",
)

panel_grid(
    "Figure 3 — Epilepsy (collaborator's figure)",
    [
        ("3a-3x", "Structure TBD. Likely follows Sharma 2024 Fig. 11's own convention:\nseverity / duration / latency bars + categorical SE-onset outcome bars.", "Box", 1),
    ],
    "fig3_box_layout.png",
    figsize=(9, 2.3),
    suptitle_note="Full box until the collaborator sends data. Data lock ~Nov 7 per the main plan's timeline.",
)

panel_grid(
    "Figure 5 — Inflammatory markers across indications",
    [
        ("5a", "Pain: wound/plasma cytokine panel, per-animal dots by arm\n[template: Gusdon 2022 Fig. 5]", "Box", 1),
        ("5b", "Epilepsy: matched cytokine panel", "Box", 1),
        ("5c", "Combined side-by-side summary, two species, same analytes", "Box", 1),
    ],
    "fig5_box_layout.png",
    suptitle_note="5a: satellite group dosed/sampled with the efficacy cohort, ~Nov 7. 5b entirely dependent on the epilepsy collaborator.",
)

panel_grid(
    "Biodistribution — conditional, not a numbered main figure",
    [
        ("Bio-a", "Study design schematic", "Have", 1),
        ("Bio-b", "Ex vivo tissue fluorescence, ipsilateral vs contralateral, paired\n[template: Porterfield Figs. 4-5]", "Box", 1),
        ("Bio-c", "Confocal colocalization, wound/DRG/cord with cell markers\n[template: Sah 2023 Fig. 1]", "Box", 1),
        ("Bio-d", "Quantified uptake, mean fluorescence intensity, n cells stated\n[template: Sharma 2024 Figs. 5/6/8]", "Box", 1),
    ],
    "fig_bio_box_layout.png",
    suptitle_note="Promoted to a main-text figure only if Cy5 QC passes and the effect is strong. Modest result -> one Limitations sentence, no figure. Negative -> omitted entirely.",
)

print("Saved box layouts for Figures 1, 2, 3, 5, and biodistribution.")
