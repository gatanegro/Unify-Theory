# Simulate Collatz sequences interacting with a dynamic FIELD density

# Initialize FIELD grid for density interactions
GRID_SIZE = 50  # Size of the FIELD grid
FIELD = np.ones((GRID_SIZE, GRID_SIZE)) * 0.5  # Uniform density at start

# Parameters for FIELD interaction
DENSITY_DECAY = 0.01  # Energy dissipation rate
ENERGY_TRANSFER = 0.05  # Energy interaction rate

# Function to update FIELD density based on Collatz number positions
def update_field_density(field, x, y, energy):
    field[x % GRID_SIZE, y % GRID_SIZE] += energy * ENERGY_TRANSFER
    field -= field * DENSITY_DECAY  # Dissipation effect
    field[field < 0] = 0  # Prevent negative densities
    return field

# Function to map Collatz sequences to FIELD interactions
def simulate_field_interaction(start_number, steps=200):
    x, y = GRID_SIZE // 2, GRID_SIZE // 2  # Start at center of FIELD
    field = FIELD.copy()
    sequence = collatz_sequence(start_number)
    trajectory = [(x, y)]

    for step, num in enumerate(sequence[:steps]):
        energy = np.log2(num + 1)  # Map number to FIELD energy
        x += int(np.sin(step) * 3)  # Dynamic movement
        y += int(np.cos(step) * 3)
        field = update_field_density(field, x, y, energy)
        trajectory.append((x % GRID_SIZE, y % GRID_SIZE))

    return field, trajectory

# Run simulation for a single Collatz sequence
start_number = 27  # Starting value for Collatz sequence
final_field, trajectory = simulate_field_interaction(start_number)

# Visualize the FIELD density after simulation
plt.figure(figsize=(8, 8))
plt.imshow(final_field, cmap="viridis", extent=[0, GRID_SIZE, 0, GRID_SIZE])
plt.colorbar(label="FIELD Density")
plt.title(f"FIELD Density After Collatz Simulation (Start: {start_number})", fontsize=14)
plt.xlabel("X Coordinate", fontsize=12)
plt.ylabel("Y Coordinate", fontsize=12)
plt.show()

# Plot the trajectory of the energy node
trajectory_x, trajectory_y = zip(*trajectory)
plt.figure(figsize=(8, 8))
plt.imshow(final_field, cmap="viridis", extent=[0, GRID_SIZE, 0, GRID_SIZE], alpha=0.6)
plt.plot(trajectory_x, trajectory_y, color="white", linewidth=1.5, label="Energy Node Path")
plt.title(f"Energy Node Path in FIELD (Start: {start_number})", fontsize=14)
plt.xlabel("X Coordinate", fontsize=12)
plt.ylabel("Y Coordinate", fontsize=12)
plt.legend()
plt.show()