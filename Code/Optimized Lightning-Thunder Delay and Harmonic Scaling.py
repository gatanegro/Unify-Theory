# Reduce the range of delays for optimized visualization
optimized_delays = [1, 2, 3, 4, 5]  # Fewer delay intervals
optimized_distances = [speed_of_sound * t for t in optimized_delays]

# Harmonic reduction of distances
optimized_harmonic_distances = [reduce_to_harmonic(int(d / 100)) for d in optimized_distances]

# Plot the optimized delay scaling
plt.figure(figsize=(8, 6))
plt.plot(optimized_delays, optimized_harmonic_distances, 'o-', label='Harmonic Reduction of Distances')
plt.title("Optimized Lightning-Thunder Delay and Harmonic Scaling", fontsize=14)
plt.xlabel("Delay (Seconds)")
plt.ylabel("Harmonic Value (1-9)")
plt.grid(True)
plt.legend()
plt.show()