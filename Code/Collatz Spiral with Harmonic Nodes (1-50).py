import numpy as np
import matplotlib.pyplot as plt

# Parameters for the spiral and harmonic mapping
theta_increment = 0.2  # Angle step for the spiral
scaling_factor = 1.1   # Scaling for spiral growth

# Generate the Collatz sequence with reduction for numbers 1 to 50
def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

# Reduce a number to harmonic scale (1-9)
def reduce_to_harmonic(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# Generate spiral points based on Collatz sequence
def generate_spiral_points(n):
    sequence = collatz_sequence(n)
    harmonics = [reduce_to_harmonic(x) for x in sequence]
    theta = 0
    radius = 1
    points = []
    for h in harmonics:
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        points.append((x, y, h))
        theta += theta_increment * h  # Harmonic affects angle step
        radius *= scaling_factor       # Scale the spiral
    return points

# Generate spiral data for numbers 1 to 50
spiral_data = []
for i in range(1, 51):
    spiral_data.extend(generate_spiral_points(i))

# Plot the spiral with nodes as high-energy points
fig, ax = plt.subplots(figsize=(8, 8))
for x, y, h in spiral_data:
    ax.scatter(x, y, c='blue', s=h*5, alpha=0.6)  # Size proportional to harmonic

# Add annotations for key numbers
key_numbers = [1, 2, 3, 4, 5, 8, 9]
for x, y, h in spiral_data:
    if h in key_numbers:
        ax.text(x, y, str(h), fontsize=8, ha='center', va='center', color='red')

# Styling the plot
ax.set_title("Collatz Spiral with Harmonic Nodes (1-50)", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_aspect('equal', 'box')
ax.grid(True)

# Display the plot
plt.show()