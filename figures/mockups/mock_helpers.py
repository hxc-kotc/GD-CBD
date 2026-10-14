"""Shared helpers for mock-data figure mockups. Every synthetic panel gets a
visible MOCK DATA watermark baked into the image - these are illustrative
shapes for layout purposes, not real measurements, and should never be
mistaken for results.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

COLOR = {"GD-CBD": "#2E7D32", "CBD": "#757575", "Vehicle": "#111111", "GD": "#5B8DB8"}
RNG = np.random.default_rng(42)


def watermark(ax, text="MOCK DATA"):
    ax.text(0.5, 0.5, text, transform=ax.transAxes, fontsize=16, color="#D32F2F",
            alpha=0.18, ha="center", va="center", rotation=28, fontweight="bold", zorder=10)


def status_tag(ax, status):
    colors = {"Have": "#2E7D32", "Partial": "#B8860B", "Box": "#9E9E9E", "Mock": "#D32F2F"}
    ax.text(0.98, 1.08, status, transform=ax.transAxes, fontsize=7.5, fontweight="bold",
            ha="right", va="bottom", color=colors.get(status, "#9E9E9E"))


def panel_letter(ax, letter, dx=-0.12, dy=1.15):
    ax.text(dx, dy, letter, transform=ax.transAxes, fontsize=13, fontweight="bold")


def empty_box(ax, title, desc, status="Box"):
    status_color = {"Have": "#2E7D32", "Partial": "#B8860B", "Box": "#9E9E9E"}
    status_face = {"Have": "#E8F5E9", "Partial": "#FFF8E1", "Box": "#F7F7F7"}
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    rect = patches.FancyBboxPatch((0.03, 0.06), 0.94, 0.88,
                                   boxstyle="round,pad=0.01,rounding_size=0.03",
                                   linewidth=1.3, edgecolor=status_color[status], facecolor=status_face[status])
    ax.add_patch(rect)
    ax.text(0.5, 0.74, title, fontsize=9, fontweight="bold", ha="center", va="top", wrap=True)
    ax.text(0.5, 0.52, desc, fontsize=7.5, ha="center", va="top", wrap=True, color="#333333")
    ax.text(0.91, 0.14, status, fontsize=8, fontweight="bold", ha="right", color=status_color[status])
