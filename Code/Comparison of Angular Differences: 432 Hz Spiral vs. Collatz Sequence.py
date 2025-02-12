# Calculate angular differences (delta angles) for both spirals

# 432 Hz Spiral Angular Differences
delta_angles_432 = np.diff(angles_432_extended_degrees)

# Collatz Sequence Angular Differences
delta_angles_collatz = np.diff(angles_collatz_extended_degrees[:len(delta_angles_432)])

# Visualization: Compare angular differences
plt.figure(figsize=(12, 6))
plt.plot(range(len(delta_angles_432)), delta_angles_432, label="432 Hz Spiral Delta Angles", color="blue")
plt.plot(range(len(delta_angles_collatz)), delta_angles_collatz, 
         label="Collatz Sequence Delta Angles", color="red", linestyle="--")

plt.title("Comparison of Angular Differences: 432 Hz Spiral vs. Collatz Sequence", fontsize=16)
plt.xlabel("Node Index (Progression)", fontsize=14)
plt.ylabel("Angular Difference (Degrees)", fontsize=14)
plt.axhline(0, color="black", linestyle="--", alpha=0.5, label="Zero Angle Change")
plt.grid(alpha=0.3)
plt.legend()
plt.show()