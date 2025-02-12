# Recreate the visualization with adjustments for clarity

# Visualize the sine wave across three cycles with proper scaling
plt.figure(figsize=(12, 8))
plt.plot(x_wave_3, y_wave_3, label="Energy Wave Across Three Cycles", color="blue")

# Mark the peak energies for each cycle
for i, peak in enumerate(peak_energies):
    # Find the peak index relative to the cycle boundaries
    cycle_start = cumulative_boundaries[i]
    cycle_end = cumulative_boundaries[i + 1]
    peak_index = np.argmax(y_wave_3[cycle_start:cycle_end]) + cycle_start
    
    plt.scatter(
        x_wave_3[peak_index],
        peak,
        color="red",
        label=f"Peak Energy Cycle {i + 1}: {peak:.2f}",
        zorder=5
    )

# Add attractor line
plt.axhline(1, color="green", linestyle="--", label="Attractor (1)")

# Adjust titles and labels for clarity
plt.title("Collatz Sequence as FIELD Oscillations Across Three Cycles", fontsize=16)
plt.xlabel("Wave Progression (Steps)", fontsize=14)
plt.ylabel("Energy (Amplitude)", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.show()