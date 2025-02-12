import matplotlib.pyplot as plt
import numpy as np

# Function to compute the Collatz sequence
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Generate Collatz sequences for multiple starting values
start_values = range(2, 101)  # Starting numbers from 2 to 100
sequences = [collatz_sequence(n) for n in start_values]

# Visualization: Plot the Collatz sequences
plt.figure(figsize=(12, 8))
for i, seq in enumerate(sequences):
    plt.plot(range(len(seq)), seq, label=f"Start: {start_values[i]}", alpha=0.6)

plt.title("Collatz Sequences: Oscillatory Dynamics", fontsize=16)
plt.xlabel("Iteration Steps", fontsize=14)
plt.ylabel("Value of n", fontsize=14)
plt.grid(alpha=0.3)
plt.yscale("log")  # Use log scale for better visualization of large values
plt.show()