# Calculate gaps between consecutive primes
prime_gaps = [primes[i] - primes[i - 1] for i in range(1, len(primes))]

# Map prime gaps to harmonic frequencies (normalize gaps)
max_gap = max(prime_gaps)
normalized_frequencies = [gap / max_gap for gap in prime_gaps]  # Normalize to [0, 1]

# Simulate harmonic relationships (map to a musical scale, e.g., octaves)
octave_scale = [freq * 2 for freq in normalized_frequencies]  # Scale frequencies into octaves

# Visualize the harmonic intervals of prime gaps
plt.figure(figsize=(12, 6))
plt.plot(range(len(octave_scale)), octave_scale, marker="o", linestyle="-", color="blue", label="Harmonic Intervals")
plt.title("Harmonic Relationships of Prime Gaps", fontsize=16)
plt.xlabel("Index (Consecutive Prime Pairs)", fontsize=14)
plt.ylabel("Harmonic Frequency (Normalized)", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.show()