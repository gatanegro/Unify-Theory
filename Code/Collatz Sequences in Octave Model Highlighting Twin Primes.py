# Highlighting twin primes in the Collatz octave plot

# Extend the range to include more numbers for a broader twin prime analysis
extended_collatz_sequences = {n: generate_collatz_sequence(n) for n in range(1, 50)}

# Recalculate positions for extended sequences
collatz_positions_density_extended = {}
for number, sequence in extended_collatz_sequences.items():
    mapped_positions = []
    for layer, value in enumerate(sequence):
        reduced_value = reduce_to_single_digit(value)
        x, y = map_to_octave(reduced_value, layer)[:2]
        z = layer * stack_spacing  # Layer height in 3D
        mapped_positions.append((x, y, z))
    collatz_positions_density_extended[number] = mapped_positions

# Highlight twin primes in the plot
collatz_positions_density_colored_twin = {}
for number, positions in collatz_positions_density_extended.items():
    colored_positions = []
    for pos in positions:
        x, y, z = pos
        original_value = int(z / stack_spacing)  # Approximate the original number
        color = 'blue' if is_twin_prime(original_value) else 'gray'
        colored_positions.append((x, y, z, color))
    collatz_positions_density_colored_twin[number] = colored_positions

# Visualize the Collatz sequences with twin primes highlighted in a broader range
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the stacked circles for reference
for i in range(num_layers):
    z_layer = i * stack_spacing  # Z-coordinate for each octave
    ax.plot(circle_x, circle_y, zs=z_layer, color='gray', linestyle='--', alpha=0.5)

# Plot each Collatz sequence as a curve with twin primes highlighted
for number, positions in collatz_positions_density_colored_twin.items():
    for x, y, z, color in positions:
        ax.scatter(x, y, z, color=color, s=50)  # Twin primes in blue

# Add labels and adjust the view
ax.set_title("Collatz Sequences in Octave Model Highlighting Twin Primes")
ax.set_xlabel("X (Horizontal Oscillation)")
ax.set_ylabel("Y (Vertical Oscillation - Scaled)")
ax.set_zlabel("Z (Octave Layer)")
plt.show()