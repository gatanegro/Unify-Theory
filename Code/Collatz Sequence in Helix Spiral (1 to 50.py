from mpl_toolkits.mplot3d import Axes3D

# Generate 3D spiral points based on Collatz sequence
def generate_helix_spiral_points(n):
    sequence = collatz_sequence(n)
    harmonics = [reduce_to_harmonic(x) for x in sequence]
    theta = 0
    radius = 1
    z = 0
    points = []
    for h in harmonics:
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        points.append((x, y, z, h))
        theta += theta_increment * h  # Harmonic affects angle step
        radius *= scaling_factor       # Scale the spiral
        z += 1  # Move upward to create a helix
    return points

# Generate helix spiral data for numbers 1 to 50
helix_data = []
for i in range(1, 51):
    helix_data.extend(generate_helix_spiral_points(i))

# Plot the helix spiral with nodes as high-energy points
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for x, y, z, h in helix_data:
    ax.scatter(x, y, z, c='blue', s=h*5, alpha=0.6)  # Size proportional to harmonic

# Add annotations for key numbers
for x, y, z, h in helix_data:
    if h in key_numbers:
        ax.text(x, y, z, str(h), fontsize=8, ha='center', va='center', color='red')

# Styling the plot
ax.set_title("Collatz Sequence in Helix Spiral (1 to 50)", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()