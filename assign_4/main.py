import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. LINK LENGTHS
L = np.array([3, 2, 1])

# 2. FIGURE SETUP
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)

line, = ax.plot([], [], 'o-', lw=4, markersize=10,
                color='royalblue', markerfacecolor='white')
time_text = ax.text(0.03, 0.93, '', transform=ax.transAxes, fontsize=10)

# 3. ANIMATION FUNCTION
def animate(i):
    # Angles (degrees → radians)
    angles = np.deg2rad([i * 5, i * 10, i * 15])
    cumulative_angles = np.cumsum(angles)

    # Forward kinematics (vectorized)
    x = np.concatenate([[0], np.cumsum(L * np.cos(cumulative_angles))])
    y = np.concatenate([[0], np.cumsum(L * np.sin(cumulative_angles))])

    line.set_data(x, y)
    time_text.set_text(
        f'θ1={i*5}°   θ2={i*10}°   θ3={i*15}°'
    )

    return line, time_text

# 4. ANIMATION
ani = FuncAnimation(
    fig,
    animate,
    frames=72,
    interval=500,
    blit=True
)

plt.title("3-Link Planar Arm Rotation", fontsize=13)
plt.show()
