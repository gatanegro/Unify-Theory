# Visualize the Collatz sequence as a wave system converging to (x1, y1)
def wave_system(sequence):
    x, y = [0], [0]  # Starting at origin (x1, y1)
    for i, num in enumerate(sequence):
        angle = i * np.pi / 10  # Phase angle (adjust for smoother curve)
        radius = np.log2(num + 1)  # Logarithmic amplitude for energy levels
        x.append(radius * np.cos(angle))
        y.append(radius * np.sin(angle))
    return x, y

# Generate the trajectory for the Collatz sequence of 27
trajectory_x, trajectory_y = wave_system(collatz_sequence_result)

# Plot the wave system
plt.figure(figsize=(8, 8))
plt.plot(trajectory_x, trajectory_y, color="blue", linewidth=1.5, label="Wave System")
plt.scatter(trajectory_x[-1], trajectory_y[-1], color="red", label="Attractor (1)", zorder=5)
plt.title("Collatz Sequence as FIELD Wave System", fontsize=16)
plt.xlabel("X Coordinate (Wave Longitude)", fontsize=12)
plt.ylabel("Y Coordinate (Wave Latitude)", fontsize=12)
plt.grid(alpha=0.3)
plt.legend()
plt.show()