# Calculate angles for the 432 Hz spiral
angles_432 = np.arctan2(y_spiral_natural, x_spiral_natural)  # Angular positions in radians
angles_432_degrees = np.degrees(angles_432)  # Convert to degrees for comparison

# Calculate angles for the Collatz spiral
x_collatz, y_collatz, z_collatz = sinusoidal_spiral(three_cycles_flat)
angles_collatz = np.arctan2(y_collatz, x_collatz)  # Angular positions in radians
angles_collatz_degrees = np.degrees(angles_collatz)  # Convert to degrees for comparison

# Visualization: Compare the angles between the 432 Hz spiral and the Collatz sequence
plt.figure(figsize=(12, 6))
plt.plot(range(len(angles_432_degrees)), angles_432_degrees, label="432 Hz Spiral Angles", color="blue")
plt.plot(range(len(angles_collatz_degrees)), angles_collatz_degrees[:len(angles_432_degrees)], 
         label="Collatz Sequence Angles", color="red", linestyle="--")

plt.title("Comparison of Angular Dynamics: 432 Hz Spiral vs. Collatz Sequence", fontsize=16)
plt.xlabel("Node Index (Progression)", fontsize=14)
plt.ylabel("Angle (Degrees)", fontsize=14)
plt.axhline(0, color="black", linestyle="--", alpha=0.5, label="Zero Angle")
plt.grid(alpha=0.3)
plt.legend()
plt.show()