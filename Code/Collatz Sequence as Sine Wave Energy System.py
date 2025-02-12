# Create a sine wave representation for the Collatz sequence based on energy packets

# Function to map Collatz sequence to sine wave points
def sine_wave_energy(sequence):
    x = np.linspace(0, len(sequence), len(sequence) * 10)  # Smooth interpolation of x values
    y = np.zeros_like(x)
    for i, num in enumerate(sequence):
        amplitude = num  # Amplitude is the energy packet value
        wave_section = np.sin(2 * np.pi * (x - i)) * amplitude  # Sine wave for this segment
        y += wave_section * np.exp(-0.2 * np.abs(x - i))  # Dampen the wave as it moves away
    return x, y

# Generate sine wave for the Collatz sequence of 27
x_wave, y_wave = sine_wave_energy(collatz_sequence_result)

# Find the peak energy point
peak_energy = np.max(y_wave)
peak_index = np.argmax(y_wave)

# Plot the sine wave energy representation
plt.figure(figsize=(12, 6))
plt.plot(x_wave, y_wave, label="Energy Wave (Collatz Sequence)", color="blue")
plt.scatter(x_wave[peak_index], peak_energy, color="red", label=f"Peak Energy: {peak_energy:.2f}", zorder=5)
plt.axhline(1, color="green", linestyle="--", label="Attractor (1)")
plt.title("Collatz Sequence as Sine Wave Energy System", fontsize=16)
plt.xlabel("Wave Progression (Steps)", fontsize=14)
plt.ylabel("Energy (Amplitude)", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.show()