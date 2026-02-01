import numpy as np
import matplotlib.pyplot as plt

# 1. BASE S-CURVE
t = np.linspace(-2, 2, 200)
x_base = t
y_base = np.sin(t)

# 2. FIGURE SETUP
plt.figure(figsize=(7, 7))
plt.axis('equal')
plt.axis('off')
plt.title("S-Curve Pattern using Rotation Principle", fontsize=13)

# 3. ROTATION LOOP
num_rotations = 60
angles = np.linspace(0, 2*np.pi, num_rotations, endpoint=False)

for theta in angles:
    cos_t, sin_t = np.cos(theta), np.sin(theta)

    x_rot = x_base * cos_t - y_base * sin_t
    y_rot = x_base * sin_t + y_base * cos_t

    plt.plot(x_rot, y_rot, color='deeppink', linewidth=0.8, alpha=0.7)

plt.show()
