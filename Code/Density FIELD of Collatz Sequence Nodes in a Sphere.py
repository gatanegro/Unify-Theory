# Generate density values for the spherical FIELD based on the Collatz sequence nodes

def collatz_field_density(numbers, points=100, field_radius=1):
    """
    Generate a density FIELD for Collatz numbers on a spherical structure.
    Numbers act as energy nodes, and the density gradient reflects their influence.
    """
    # Create spherical grid (theta, phi)
    theta = np.linspace(0, 2 * np.pi, points)  # Angular (azimuthal) range
    phi = np.linspace(0, np.pi, points)  # Polar range
    theta, phi = np.meshgrid(theta, phi)

    # Radial distance grid for the sphere
    r_grid = field_radius * np.ones_like(theta)

    # Spherical to Cartesian conversion for the FIELD grid
    x_field = r_grid * np.sin(phi) * np.cos(theta)
    y_field = r_grid * np.sin(phi) * np.sin(theta)
    z_field = r_grid * np.cos(phi)

    # Compute density based on proximity to Collatz nodes (treated as energy sources)
    density = np.zeros_like(r_grid)
    for node in numbers:
        r_node = node / max(numbers) * field_radius  # Normalize node radius
        density += np.exp(-((r_grid - r_node) ** 2) * 10)  # Exponential decay from node

    return x_field, y_field, z_field, density

# Generate density FIELD based on Collatz nodes
x_field, y_field, z_field, density_field = collatz_field_density(collatz_numbers)

# Visualize the spherical density FIELD
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x_field, y_field, z_field, c=density_field.flatten(), cmap="viridis", alpha=0.8)
cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("Energy Density", fontsize=12)

# Label axes and add details
ax.set_title("Density FIELD of Collatz Sequence Nodes in a Sphere", fontsize=16)
ax.set_xlabel("X Coordinate", fontsize=12)
ax.set_ylabel("Y Coordinate", fontsize=12)
ax.set_zlabel("Z Coordinate", fontsize=12)
plt.show()