import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Define the Collatz function
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Simulate Collatz sequences for a range of numbers
def simulate_collatz_range(start, end):
    data = defaultdict(list)
    for i in range(start, end + 1):
        sequence = collatz_sequence(i)
        data[i] = sequence
    return data

# Plot Collatz sequences for visualization
def plot_collatz_sequences(collatz_data, title="Collatz Sequences"):
    plt.figure(figsize=(10, 6))
    for key, seq in collatz_data.items():
        plt.plot(range(len(seq)), seq, label=f"Start: {key}")
    plt.xlabel("Step")
    plt.ylabel("Node Value")
    plt.title(title)
    plt.grid()
    plt.legend()
    plt.show()

# Generate Collatz data for a range of numbers
start, end = 5, 15  # Modify as needed for a broader range
collatz_data = simulate_collatz_range(start, end)

# Plot the Collatz sequences
plot_collatz_sequences(collatz_data, title="Collatz Sequences: Growth and Collapse Dynamics")
Always show details
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Define the Collatz function
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Simulate Collatz sequences for a range of numbers
def simulate_collatz_range(start, end):
    data = defaultdict(list)
    for i in range(start, end + 1):
        sequence = collatz_sequence(i)
        data[i] = sequence
    return data

# Plot Collatz sequences for visualization
def plot_collatz_sequences(collatz_data, title="Collatz Sequences"):
    plt.figure(figsize=(10, 6))
    for key, seq in collatz_data.items():
        plt.plot(range(len(seq)), seq, label=f"Start: {key}")
    plt.xlabel("Step")
    plt.ylabel("Node Value")
    plt.title(title)
    plt.grid()
    plt.legend()
    plt.show()

# Generate Collatz data for a range of numbers
start, end = 5, 15  # Modify as needed for a broader range
collatz_data = simulate_collatz_range(start, end)

# Plot the Collatz sequences
plot_collatz_sequences(collatz_data, title="Collatz Sequences: Growth and Collapse Dynamics")
