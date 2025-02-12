# Reverse engineering angular momentum for the Collatz sequence spiral

# Define constants for angular velocity scaling
ANGULAR_SCALING = 2 * np.pi / 10  # Adjust angular velocity per step

# Function to calculate angular momentum
def calculate_angular_momentum(sequence):
    r_values = [np.log2(num + 1) for num in sequence]  # Radius as energy amplitude
    angular_momenta = []
    for i, r in enumerate(r_values):
        # Angular velocity (rate of angular progression)
        angular_velocity = ANGULAR_SCALING * (i + 1)
        # Effective mass is proportional to energy (sequence value)
        mass = sequence[i]
        # Angular momentum: L = r * m * v
        angular_momentum = r * mass * angular_velocity
        angular_momenta.append(angular_momentum)
    return angular_momenta

# Compute angular momentum for three cycles
angular_momenta_3_cycles = calculate_angular_momentum(three_cycles_flat)

# Visualize angular momentum over the spiral's progression
plt.figure(figsize=(12, 6))
plt.plot(range(len(angular_momenta_3_cycles)), angular_momenta_3_cycles, color="purple", label="Angular Momentum (L)")
plt.title("Angular Momentum Evolution in Collatz Spiral", fontsize=16)
plt.xlabel("Step in Sequence", fontsize=14)
plt.ylabel("Angular Momentum (L)", fontsize=14)
plt.axhline(0, color="black", linestyle="--", label="Equilibrium Line")
plt.grid(alpha=0.3)
plt.legend()
plt.show()