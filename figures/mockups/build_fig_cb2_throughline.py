"""
CB2-overexpression-after-insult throughline — NEW, built 2026-11-03 per the
2026-11-02 PI working session. The single biggest structural addition from
that meeting: Sujatha wants the paper to show the target (CB2) goes up after
the insult in each of the three systems the paper uses, so that treating with
a CB2 agonist is mechanistically justified rather than asserted - "we have to
show that the target is there and we're going after the target... therefore
this, which is a stronger CB2 agonist, works better than CBD."

Built as one cross-model panel row (the user's choice over scattering this
into all three main figures) - reads as the throughline Sujatha described:
"in some fashion between the 3 models we should kind of show [CB2
expression]." Deliberately NOT a quantified, powered experiment: "either
Western or immuno, whichever... don't try to quantify or do too much, just
show like an image and say it's more, it's less, that's good enough." Not a
gate either - "I don't think the paper has to be held up for it."

Placement: not yet assigned a figure number. This is new content with no
existing figure to attach to; where it lives (its own small figure, or
folded as an extra row into Figure 2) is part of the still-pending
renumbering pass (see INTEGRATION_PLAN_2026-11-02.md section 6, "not
recommended... renumbering figures again" until the cut/rebuild pass is
done). All three panels are mock - no stain or blot has been run yet.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mock_helpers import watermark, status_tag, panel_letter, RNG

fig = plt.figure(figsize=(11, 4.4))
fig.suptitle("CB₂ overexpression after insult — cross-model throughline (MOCKUP, placement pending)", fontsize=13, fontweight="bold", x=0.02, ha="left", y=0.98)
fig.text(0.02, 0.9, "Existing material in all three cases - cheap stains/blots on tissue or cells already in hand, not a new study. Not a gate on the paper.",
         fontsize=8.5, color="#555555", style="italic")
gs = GridSpec(1, 3, figure=fig, wspace=0.35, top=0.78, bottom=0.2, left=0.06, right=0.97)

panels = [
    ("Microglia (in vitro)", "Naive", "+ LPS", "BV2/HMC3", "ax_mg"),
    ("Incision model (DRG)", "Naive", "Injured", "DRG neurons + glia", "ax_drg"),
    ("Seizure model", "Naive", "Post-SE", "Hippocampal/cortical neurons", "ax_se"),
]

for i, (title, cond1, cond2, material, _) in enumerate(panels):
    ax = fig.add_subplot(gs[0, i])
    baseline = RNG.uniform(0.8, 1.2)
    insult = baseline * RNG.uniform(2.2, 3.4)
    vals = [baseline, insult]
    err = [baseline * 0.2, insult * 0.25]
    x = np.arange(2)
    ax.bar(x, vals, yerr=err, color=["#9E9E9E", "#2E7D32"], width=0.5, capsize=4, edgecolor="white")
    ax.set_xticks(x); ax.set_xticklabels([cond1, cond2], fontsize=8.5)
    ax.set_ylabel("CB₂ expression (rel. units)", fontsize=7.5)
    ax.set_title(f"{title}\n({material})", fontsize=8.5)
    watermark(ax, "MOCK")
    panel_letter(ax, chr(ord("a") + i))
    status_tag(ax, "Box")

fig.text(0.02, 0.02,
         "CB2 overexpression after insult, shown separately in each of the three systems this paper uses. (a) Microglia, naive vs. LPS-exposed. (b) DRG "
         "neurons and glia, naive vs. injured (flank incision). (c) Hippocampal/cortical neurons, naive vs. post-status-epilepticus. Either Western blot or "
         "immunostaining, whichever is more practical per system - this is deliberately not a quantified, powered comparison, just evidence the target goes "
         "up. All three panels are mock; no stain or blot has been run yet. This content has no figure number yet - see the main plan's Open items.",
         fontsize=7, color="#555555", wrap=True)
plt.savefig("/home/user/gd-cbd/figures/mockups/fig_cb2_throughline.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved fig_cb2_throughline.png (3 panels: a-c)")
