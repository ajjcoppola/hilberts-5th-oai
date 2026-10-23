#!/usr/bin/env python3
"""Draw the two p-adic solenoid figures for the development-story essay.

AI-assisted / AI-generated with Cursor (Grok, Anthropic, and OpenAI models).
Direction: Alan J. Coppola.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parents[1] / "docs" / "figures"
BG = "#faf8f5"
INK = "#1a1a1a"
ACCENT = "#8b3a2a"
MUTED = "#5a534c"
BLUE = "#3d5a80"


def _style_2d(ax):
    ax.set_facecolor(BG)
    ax.set_aspect("equal")
    ax.axis("off")


def torus_coords(R, r, u, v):
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    return x, y, z


def winding_centerline(p, k, R, a, n=4000):
    t = np.linspace(0, 2 * np.pi, n)
    winds = p**k
    return torus_coords(R, a, t, winds * t)


def tube_around(x, y, z, radius, n_circ=18, step=8):
    pts = np.stack([x, y, z], axis=1)
    d = np.gradient(pts, axis=0)
    T = d / (np.linalg.norm(d, axis=1, keepdims=True) + 1e-12)
    n0 = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(T[0], n0)) > 0.9:
        n0 = np.array([0.0, 1.0, 0.0])
    N = np.zeros_like(T)
    B = np.zeros_like(T)
    n = n0 - np.dot(n0, T[0]) * T[0]
    n /= np.linalg.norm(n)
    N[0] = n
    B[0] = np.cross(T[0], n)
    for i in range(1, len(T)):
        n = N[i - 1] - np.dot(N[i - 1], T[i]) * T[i]
        n /= np.linalg.norm(n) + 1e-12
        N[i] = n
        B[i] = np.cross(T[i], n)
    theta = np.linspace(0, 2 * np.pi, n_circ)
    idx = np.arange(0, len(x), step)
    xs = np.zeros((n_circ, len(idx)))
    ys = np.zeros_like(xs)
    zs = np.zeros_like(xs)
    for j, i in enumerate(idx):
        xs[:, j] = x[i] + radius * (N[i, 0] * np.cos(theta) + B[i, 0] * np.sin(theta))
        ys[:, j] = y[i] + radius * (N[i, 1] * np.cos(theta) + B[i, 1] * np.sin(theta))
        zs[:, j] = z[i] + radius * (N[i, 2] * np.cos(theta) + B[i, 2] * np.sin(theta))
    return xs, ys, zs


def draw_solenoid_picture(path: Path, p: int = 2):
    R, r = 3.2, 1.05
    fig = plt.figure(figsize=(10.2, 6.6), facecolor=BG)
    ax = fig.add_subplot(121, projection="3d")
    ax_disk = fig.add_subplot(122)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.10, top=0.86, wspace=0.08)

    u = np.linspace(0, 2 * np.pi, 70)
    v = np.linspace(0, 2 * np.pi, 36)
    uu, vv = np.meshgrid(u, v)
    tx, ty, tz = torus_coords(R, r, uu, vv)
    ax.plot_surface(
        tx, ty, tz, color="#ddd4c8", alpha=0.18, linewidth=0, shade=True, zorder=0
    )
    # a few wire rings so the donut reads
    for ui in np.linspace(0, 2 * np.pi, 16, endpoint=False):
        rx, ry, rz = torus_coords(R, r, ui, v)
        ax.plot(rx, ry, rz, color="#cfc6bb", lw=0.5, alpha=0.85)
    for vi in np.linspace(0, 2 * np.pi, 10, endpoint=False):
        rx, ry, rz = torus_coords(R, r, u, vi)
        ax.plot(rx, ry, rz, color="#cfc6bb", lw=0.4, alpha=0.7)

    stages = [
        (1, 0.52, 0.22, ACCENT, f"stage 1: winds {p} times"),
        (2, 0.28, 0.10, BLUE, f"stage 2: winds {p**2} times"),
        (3, 0.14, 0.045, INK, f"stage 3: winds {p**3} times"),
    ]
    for k, a, rad, color, lab in stages:
        x, y, z = winding_centerline(p, k, R, a)
        xs, ys, zs = tube_around(x, y, z, rad)
        ax.plot_surface(xs, ys, zs, color=color, alpha=0.92, linewidth=0, shade=True)
        ax.plot([np.nan], [np.nan], [np.nan], color=color, lw=3, label=lab)

    ax.view_init(elev=26, azim=-52)
    try:
        ax.set_proj_type("ortho")
    except Exception:
        pass
    ax.set_box_aspect((1, 1, 0.55))
    lim = R + r
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-r * 1.35, r * 1.35)
    ax.set_facecolor(BG)
    ax.patch.set_facecolor(BG)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor(BG)
        axis.pane.set_edgecolor(BG)
        axis.pane.set_alpha(1.0)
        axis.line.set_color(BG)
        axis.set_ticklabels([])
    ax.grid(False)
    ax.set_axis_off()
    ax.legend(
        loc="lower left",
        bbox_to_anchor=(0.0, 0.0),
        frameon=False,
        fontsize=9,
        labelcolor=INK,
        prop={"family": "Georgia"},
    )

    # Meridional disk: nested p-adic disks (Cantor in the fiber)
    _style_2d(ax_disk)
    ax_disk.set_xlim(-1.25, 1.25)
    ax_disk.set_ylim(-1.25, 1.45)
    ax_disk.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#c4b8aa", lw=1.6))
    ax_disk.text(0, 1.28, "a meridional disk", ha="center", fontsize=11, color=MUTED, fontname="Georgia")

    palette = [ACCENT, BLUE, INK]

    def nested_disks(cx, cy, rad, depth, p, stage):
        color = palette[min(stage, len(palette) - 1)]
        if depth == 0:
            ax_disk.add_patch(
                Circle((cx, cy), rad, facecolor=color, edgecolor=INK, lw=0.4, alpha=0.9)
            )
            return
        for j in range(p):
            ang = j * 2 * np.pi / p
            offset = rad * 0.50
            nx = cx + offset * np.cos(ang)
            ny = cy + offset * np.sin(ang)
            child = rad * 0.38
            ax_disk.add_patch(
                Circle((nx, ny), child, fill=False, edgecolor=color, lw=1.4)
            )
            nested_disks(nx, ny, child, depth - 1, p, stage + 1)

    nested_disks(0, 0, 1.0, 3, p, 0)
    ax_disk.text(
        0,
        -1.18,
        f"p = {p} disks at each stage.\nThe fiber is a Cantor set.",
        ha="center",
        va="top",
        fontsize=9,
        color=MUTED,
        fontname="Georgia",
    )

    fig.suptitle(
        f"The {p}-adic solenoid, nested in a solid torus",
        fontname="Georgia",
        fontsize=16,
        color=ACCENT,
        y=0.97,
    )
    fig.text(
        0.5,
        0.03,
        "Each stage is a thinner solid torus, wound p times inside the last. "
        "The solenoid is the infinite nested intersection.",
        ha="center",
        fontsize=10,
        fontname="Georgia",
        color=MUTED,
    )
    fig.savefig(path, dpi=200, facecolor=BG)
    fig.savefig(path.with_suffix(".svg"), facecolor=BG)
    plt.close(fig)


def _circle(ax, cx, cy, r, color=INK, lw=1.8):
    ax.add_patch(
        Circle(
            (cx, cy),
            r,
            fill=False,
            edgecolor=color,
            linewidth=lw,
            zorder=3,
        )
    )
    ax.add_patch(
        Circle((cx + r * 0.62, cy), 3.2, facecolor=color, edgecolor="none", zorder=4)
    )


def _arrow(ax, x1, y1, x2, y2, color=INK):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=14,
            lw=1.4,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def draw_inverse_limit(path: Path, p: int = 2):
    fig, ax = plt.subplots(figsize=(11.0, 6.4), facecolor=BG)
    ax.set_xlim(0, 1100)
    ax.set_ylim(0, 640)
    _style_2d(ax)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    ax.text(
        550,
        600,
        "The p-adic solenoid as an inverse limit of ×p maps",
        ha="center",
        va="center",
        fontsize=16,
        fontname="Georgia",
        color=ACCENT,
    )

    xs = [150, 400, 650, 900]
    cy = 390
    r = 58
    stage_groups = [rf"$C_{{p}}$", rf"$C_{{p^2}}$", rf"$C_{{p^3}}$", rf"$C_{{p^4}}$"]
    rotations = [
        r"rotate by $1/p$",
        r"rotate by $1/p^{2}$",
        r"rotate by $1/p^{3}$",
        r"rotate by $1/p^{4}$",
    ]

    for i, cx in enumerate(xs):
        _circle(ax, cx, cy, r, color=INK if i else ACCENT, lw=2.0 if i else 2.4)
        ax.text(
            cx,
            cy - r - 22,
            r"$S^1$",
            ha="center",
            va="top",
            fontsize=13,
            color=INK,
        )
        # rotation action arrow
        ax.annotate(
            "",
            xy=(cx + 18, cy + r + 8),
            xytext=(cx - 18, cy + r + 8),
            arrowprops=dict(
                arrowstyle="-|>",
                color=BLUE,
                lw=1.3,
                connectionstyle="arc3,rad=-0.7",
            ),
        )
        ax.text(
            cx,
            cy + r + 48,
            stage_groups[i],
            ha="center",
            va="bottom",
            fontsize=12,
            color=BLUE,
        )
        ax.text(
            cx,
            cy + r + 28,
            rotations[i],
            ha="center",
            va="bottom",
            fontsize=8.5,
            color=BLUE,
        )

    for i in range(len(xs) - 1):
        x1 = xs[i + 1] - r - 8
        x2 = xs[i] + r + 8
        _arrow(ax, x1, cy, x2, cy, color=ACCENT)
        ax.text(
            (xs[i] + xs[i + 1]) / 2,
            cy + 18,
            r"$\times p$",
            ha="center",
            va="bottom",
            fontsize=13,
            color=ACCENT,
        )

    ax.text(xs[-1] + r + 28, cy, r"$\cdots$", ha="left", va="center", fontsize=18, color=INK)

    # Cantor fiber under the coarsest circle
    ax.text(
        550,
        248,
        r"A point of $\Sigma_p$ is a coherent sequence $(z_0,z_1,z_2,\ldots)$ with $z_n = p\cdot z_{n+1}$ on $\mathbb{R}/\mathbb{Z}$.",
        ha="center",
        va="center",
        fontsize=11,
        color=INK,
    )

    # fiber sketch
    fy = 145
    ax.text(70, fy + 38, "one fiber", ha="center", va="bottom", fontsize=9, color=MUTED, fontname="Georgia")
    # p=2 shown: 1, then 2, then 4, then 8 ticks on a line
    fiber_xs = [150, 400, 650, 900]
    counts = [1, p, p**2, min(p**3, 8)]
    for cx, count in zip(fiber_xs, counts):
        spread = 36 if count > 1 else 0
        ys = np.linspace(fy - spread, fy + spread, count) if count > 1 else [fy]
        for y in ys:
            ax.add_patch(Circle((cx, y), 4.5, facecolor=INK, edgecolor="none"))
        if count > 1:
            ax.plot([cx, cx], [min(ys), max(ys)], color="#cfc6bb", lw=1.0, zorder=1)

    for i in range(len(fiber_xs) - 1):
        _arrow(ax, fiber_xs[i + 1] - 22, fy, fiber_xs[i] + 22, fy, color="#c4b8aa")

    ax.add_patch(
        FancyBboxPatch(
            (40, 18),
            1020,
            70,
            boxstyle="round,pad=6,rounding_size=6",
            facecolor="#fff",
            edgecolor="#d7cfc4",
            linewidth=1.0,
        )
    )
    ax.text(
        550,
        53,
        r"Inverse limit of the circles under $\times p$ is the solenoid $\Sigma_p$."
        "\n"
        r"Inverse limit of the rotations is a free action of the $p$-adic integers $\mathbb{Z}_p$.",
        ha="center",
        va="center",
        fontsize=12,
        color=INK,
    )

    fig.savefig(path, dpi=200, facecolor=BG)
    fig.savefig(path.with_suffix(".svg"), facecolor=BG)
    plt.close(fig)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    solenoid = OUT / "padic_solenoid.png"
    inv = OUT / "padic_solenoid_inverse_limit.png"
    draw_solenoid_picture(solenoid, p=2)
    draw_inverse_limit(inv, p=2)
    print(solenoid)
    print(inv)


if __name__ == "__main__":
    main()
