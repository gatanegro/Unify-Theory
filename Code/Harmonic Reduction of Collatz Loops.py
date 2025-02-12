# Visualize detailed loops and their harmonic reductions
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Plot original Collatz loops
for key, loops in adjusted_collatz_loops.items():
    x = [key] * len(loops)
    y = [sum(loop) for loop in loops]
    axes[0].scatter(x, y, alpha=0.7, label=f"Start {key}" if key <= 3 else "")

axes[0].set_title("Original Collatz Loops (Sum of Triplets)", fontsize=14)
axes[0].set_xlabel("Starting Number")
axes[0].set_ylabel("Sum of Triplets (a+b+c)")
axes[0].grid(True)
axes[0].legend()

# Plot harmonic-reduced Collatz loops
for key, loops in adjusted_harmonic_loops.items():
    x = [key] * len(loops)
    y = [sum(loop) for loop in loops]
    axes[1].scatter(x, y, alpha=0.7, label=f"Start {key}" if key <= 3 else "")

axes[1].set_title("Harmonic Reduction of Collatz Loops", fontsize=14)
axes[1].set_xlabel("Starting Number")
axes[1].set_ylabel("Sum of Harmonic Triplets (a+b+c)")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()

# Analyze scaling patterns and abc conjecture connection
scaling_patterns = []
abc_relations = []

for key, loops in adjusted_harmonic_loops.items():
    for triplet in loops:
        a, b, c = triplet
        scaling_patterns.append((a, b, c))
        if a + b == c:
            abc_relations.append((a, b, c))

scaling_patterns[:5], abc_relations[:5]  # Show first few patterns and abc-related triplets