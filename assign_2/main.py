import numpy as np
import matplotlib.pyplot as plt

# 1. ORIGINAL SHAPE COORDINATES
points = np.array([
    [40, 10],
    [50, 10],
    [50, 30],
    [45, 40],
    [40, 20],
    [40, 10]   # Close the shape
])

# 2. ROTATION SETUP
theta_deg = 45
theta_rad = np.radians(theta_deg)

# Rotation matrix (about origin)
R = np.array([
    [np.cos(theta_rad), -np.sin(theta_rad)],
    [np.sin(theta_rad),  np.cos(theta_rad)]
])

# Apply rotation
rotated_points = points @ R.T

# 3. PLOTTING
plt.figure(figsize=(6, 6))

# Original shape
plt.plot(points[:, 0], points[:, 1],
         'b--', linewidth=2, marker='o', label='Original')

# Rotated shape
plt.plot(rotated_points[:, 0], rotated_points[:, 1],
         'r-', linewidth=2, marker='o', label=f'Rotated {theta_deg}°')

# Axes & grid
plt.axhline(0, color='black', linewidth=0.6)
plt.axvline(0, color='black', linewidth=0.6)
plt.plot(0, 0, 'ko', label='Origin (0,0)')

plt.grid(True, linestyle='--', alpha=0.6)
plt.axis('equal')
plt.legend()
plt.title(f"Absolute Rotation of Hut ({theta_deg}°)")

plt.show()

# 4. PRINT COORDINATES
print(f"\n--- Coordinates after {theta_deg}° Rotation ---")
labels = ["Bottom Left", "Bottom Right", "Top Right", "Peak", "Top Left"]

for label, (x, y) in zip(labels, rotated_points[:-1]):
    print(f"{label}: ({x:.2f}, {y:.2f})")
