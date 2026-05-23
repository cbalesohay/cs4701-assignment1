import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from models.track import Track
from models.node import Node

def visualize(grid, track: Track):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Build RGBA image
    display = np.ones((40, 40, 4))

    # Explored cells — grey
    for (r, c) in track.closed_list:
        display[r, c] = [0.6, 0.6, 0.6, 1.0]

    # Start — green, end — red
    display[track.start.position[0], track.start.position[1]] = [0.0, 0.8, 0.0, 1.0]
    display[track.end.position[0],  track.end.position[1]]  = [0.8, 0.0, 0.0, 1.0]

    ax.imshow(display, origin="upper", interpolation="nearest")

    # Grid that displays the terrain
    for r in range(40):
        for c in range(40):
            ax.text(c, r, str(grid[r][c].char), ha="center", va="center", color="black", fontsize=8)

    # Backtrack from goal node through parent pointers
    path = []
    goal_node = track.closed_list.get(track.end.position)
    if goal_node:
        current = goal_node
        while current is not None:
            path.append(current)
            current = current.parent
        path.reverse()
        path_rows = [p.position[0] for p in path]
        path_cols = [p.position[1] for p in path]
        ax.plot(path_cols, path_rows, color="blue", linewidth=2, zorder=10)

    ax.set_title(f"Path length: {len(path)}  |  Cells explored: {len(track.closed_list)}")

    from matplotlib.patches import Patch
    ax.legend(handles=[
        Patch(color=(0, 0.8, 0), label="Start"),
        Patch(color=(0.8, 0, 0), label="end"),
        Patch(color=(0.6, 0.6, 0.6), label="Explored"),
    ])

    plt.tight_layout()
    plt.show()