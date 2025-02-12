from mpl_toolkits.mplot3d import Axes3D

# Create a 3D spiral visualization for the Collatz sequence across three cycles
def spiral_wave(sequence):
    theta = np.linspace(0, 2 * np.pi * len(sequence), len(sequence))  # Angular progression
    z = -np.linspace(0, len(sequence), len(sequence))  # Vertical progression (downward spiral)
    r = [np.log2(num + 1) for num in sequence]  # Radius as energy amplitude
    x = r * np.cos(theta)  # X-coordinate in 3D
    y = r * np.sin(theta)  # Y-coordinate in 3D
    return x, y, z

# Generate the 3D spiral for three Collatz cycles
x_spiral, y_spiral, z_spiral = spiral_wave(three_cycles_flat)

# Visualize the 3D spiral
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_spiral, y_spiral, z_spiral, color="blue", label="Energy Spiral (Collatz Sequence)")
ax.scatter(x_spiral[0], y_spiral[0], z_spiral[0], color="red", label="Start (1)", s=100)
ax.scatter(x_spiral[-1], y_spiral[-1], z_spiral[-1], color="green", label="End (Attractor)", s=100)

# Labeling and adjustments
ax.set_title("Collatz Sequence as a 3D Spiral", fontsize=16)
ax.set_xlabel("X (Wave Longitude)", fontsize=12)
ax.set_ylabel("Y (Wave Latitude)", fontsize=12)
ax.set_zlabel("Z (Cycle Progression)", fontsize=12)
ax.legend()
plt.show()