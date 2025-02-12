import numpy as np
import matplotlib.pyplot as plt

# Simulate fractal patterns for lightning and wave propagation for thunder

# 1. Lightning: Fractal branching structure using recursion
def lightning_branch(start, length, angle, depth):
    if depth == 0:
        return [start]
    x, y = start
    end1 = (x + length * np.cos(angle), y + length * np.sin(angle))
    end2 = (x + length * np.cos(angle + np.pi / 6), y + length * np.sin(angle + np.pi / 6))
    return [start] + lightning_branch(end1, length * 0.7, angle - np.pi / 12, depth - 1) + \
           lightning_branch(end2, length * 0.7, angle + np.pi / 12, depth - 1)

# Generate lightning fractal
lightning_pattern = lightning_branch((0, 0), length=1, angle=-np.pi / 2, depth=6)

# 2. Thunder: Spherical wave propagation using harmonic oscillations
theta = np.linspace(0, 2 * np.pi, 500)
wave_amplitudes = [np.sin(2 * np.pi * freq * theta) for freq in range(1, 5)]

# Plot Lightning and Thunder
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Lightning fractal visualization
for i in range(len(lightning_pattern) - 1):
    x1, y1 = lightning_pattern[i]
    x2, y2 = lightning_pattern[i + 1]
    axes[0].plot([x1, x2], [y1, y2], color='blue', lw=1)
axes[0].set_title("Fractal Lightning Pattern", fontsize=14)
axes[0].set_aspect('equal')
axes[0].grid(True)

# Thunder wave propagation visualization
for i, wave in enumerate(wave_amplitudes):
    axes[1].plot(theta, wave + i, label=f'Freq {i+1}')
axes[1].set_title("Thunder: Harmonic Wave Propagation", fontsize=14)
axes[1].set_xlabel("Angle (Radians)")
axes[1].set_ylabel("Amplitude")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()