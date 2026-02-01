import numpy as np
import matplotlib.pyplot as plt


def plot_robotic_arm(L1=110.0, L2=140.0, theta1=90, theta2=180):

    # Convert degrees to radians
    t1 = np.deg2rad(theta1)
    t2 = np.deg2rad(theta2)

    # Joint coordinates (forward kinematics)
    x = np.array([
        0,
        L1 * np.cos(t1),
        L1 * np.cos(t1) + L2 * np.cos(t1 + t2)
    ])

    y = np.array([
        0,
        L1 * np.sin(t1),
        L1 * np.sin(t1) + L2 * np.sin(t1 + t2)
    ])

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot links
    ax.plot(x[:2], y[:2], 'b-', linewidth=3, label=f'L1 = {L1:.1f} mm')
    ax.plot(x[1:], y[1:], 'r-', linewidth=3, label=f'L2 = {L2:.1f} mm')

    # Plot joints
    ax.scatter(x, y, c=['blue', 'red', 'green'], s=80, zorder=3)

    # Annotate joints
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.text(xi + 5, yi + 5, f'J{i+1} ({xi:.1f}, {yi:.1f})', fontsize=9)

    # Formatting
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)

    limit = L1 + L2 + 20
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    ax.set_title("2D Robotic Arm (Forward Kinematics)")
    ax.legend(fontsize='small')

    plt.show()


if __name__ == "__main__":
    plot_robotic_arm()
