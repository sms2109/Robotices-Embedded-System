import matplotlib.pyplot as plt
import numpy as np


def plot_robotic_arm():
    L1 = 110.0
    L2 = 140.0

    # Joint coordinates
    lx = np.array([0.0, 0.0, -L2])
    ly = np.array([0.0, L1, L1])

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor('white')

    # Plot links
    ax.plot(lx[:2], ly[:2], 'b-', linewidth=2, label=f'L1 = {L1:.2f} mm')
    ax.plot(lx[1:], ly[1:], 'r-', linewidth=2, label=f'L2 = {L2:.2f} mm')

    # Plot joints (loop instead of repetition)
    colors = ['b', 'r', 'g']
    for i in range(3):
        ax.plot(
            lx[i], ly[i],
            colors[i] + 'o',
            markersize=8,
            label=f'Joint {i+1}: ({lx[i]:.1f}, {ly[i]:.1f})'
        )

    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)

    limit = 200
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    ax.set_title("2D Robotic Arm Layout")
    ax.legend(loc='upper right', fontsize='small')

    plt.show()


if __name__ == "__main__":
    plot_robotic_arm()
