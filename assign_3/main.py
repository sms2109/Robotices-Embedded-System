import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. HUT SHAPE (CLOSED POLYGON)
points = np.array([
    [40, 10],
    [50, 10],
    [50, 30],
    [45, 40],
    [40, 20],
    [40, 10]
])

# 2. FIGURE SETUP
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-70, 70)
ax.set_ylim(-70, 70)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)

line, = ax.plot([], [], 'b-o', linewidth=2)
fill = ax.fill([], [], color='green', alpha=0.35)[0]

# 3. ANIMATION UPDATE FUNCTION
def update(angle):
    rad = np.radians(angle)

    # Rotation matrix (same math, cleaner)
    R = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad),  np.cos(rad)]
    ])

    rotated = points @ R.T

    line.set_data(rotated[:, 0], rotated[:, 1])
    fill.set_xy(rotated)

    ax.set_title(f"Absolute Rotation : {angle}°", fontsize=12)
    return line, fill

# 4. ANIMATION
ani = FuncAnimation(
    fig,
    update,
    frames=np.arange(0, 360, 5),
    interval=50,
    blit=True
)

plt.show()
