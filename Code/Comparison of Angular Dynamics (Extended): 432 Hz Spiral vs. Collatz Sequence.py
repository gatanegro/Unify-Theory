# Expand the analysis to include larger ranges for both systems

# Generate extended numbers for 432 Hz spiral (up to 100 nodes)
extended_numbers = range(1, 101)
x_spiral_extended, y_spiral_extended, z_spiral_extended = sinusoidal_spiral_with_frequency(extended_numbers, natural_frequencies * 2)

# Extend the Collatz sequence spiral for comparison
extended_collatz_sequence = three_cycles_flat * 2  # Repeat the sequence for extended comparison
x_collatz_extended, y_collatz_extended, z_collatz_extended = sinusoidal_spiral(extended_collatz_sequence)

# Calculate angles for extended ranges
angles_432_extended = np.arctan2(y_spiral_extended, x_spiral_extended)
angles_432_extended_degrees = np.degrees(angles_432_extended)

angles_collatz_extended = np.arctan2(y_collatz_extended, x_collatz_extended)
angles_collatz_extended_degrees = np.degrees(angles_collatz_extended)

# Visualization: Compare the extended angular dynamics
plt.figure(figsize=(12, 6))
plt.plot(range(len(angles_432_extended_degrees)), angles_432_extended_degrees, 
         label="432 Hz Spiral Angles (Extended)", color="blue")
plt.plot(range(len(angles_collatz_extended_degrees)), angles_collatz_extended_degrees[:len(angles_432_extended_degrees)], 
         label="Collatz Sequence Angles (Extended)", color="red", linestyle="--")

plt.title("Comparison of Angular Dynamics (Extended): 432 Hz Spiral vs. Collatz Sequence", fontsize=16)
plt.xlabel("Node Index (Progression)", fontsize=14)
plt.ylabel("Angle (Degrees)", fontsize=14)
plt.axhline(0, color="black", linestyle="--", alpha=0.5, label="Zero Angle")
plt.grid(alpha=0.3)
plt.legend()
plt.show()