# Function to generate Collatz sequence for multiple cycles (from 1 to 1 again)
def collatz_three_cycles(start):
    cycles = []
    current_cycle = []
    while len(cycles) < 3:
        current_cycle.append(start)
        if start == 1 and current_cycle not in cycles:  # Complete a cycle when 1 is reached
            cycles.append(current_cycle)
            current_cycle = []
        if start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1
    return cycles

# Generate three cycles of Collatz sequence starting from 1
three_cycles = collatz_three_cycles(1)
three_cycles_flat = [num for cycle in three_cycles for num in cycle]  # Flatten for wave mapping

# Generate sine wave for the three cycles
x_wave_3, y_wave_3 = sine_wave_energy(three_cycles_flat)

# Find the peak energy points for each cycle
cycle_boundaries = [0] + [len(cycle) for cycle in three_cycles]
cumulative_boundaries = np.cumsum(cycle_boundaries)
peak_energies = [np.max(y_wave_3[cumulative_boundaries[i]:cumulative_boundaries[i + 1]]) for i in range(3)]

# Visualize the sine wave across three cycles
plt.figure(figsize=(12, 8))
plt.plot(x_wave_3, y_wave_3, label="Energy Wave Across Three Cycles", color="blue")
for i, peak in enumerate(peak_energies):
    plt.scatter(
        x_wave_3[np.argmax(y_wave_3[cumulative_boundaries[i]:cumulative_boundaries[i + 1]])],
        peak,
        color="red",
        label=f"Peak Energy Cycle {i + 1}: {peak:.2f}",
        zorder=5
    )
plt.axhline(1, color="green", linestyle="--", label="Attractor (1)")
plt.title("Collatz Sequence Across Three Cycles", fontsize=16)
plt.xlabel("Wave Progression (Steps)", fontsize=14)
plt.ylabel("Energy (Amplitude)", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.show()