# Simulate and analyze even-odd scaling convergence to 1

def collatz_even_odd_convergence(start, max_steps=100):
    """
    Simulates the Collatz sequence starting from a number and tracks the steps until 1.
    Returns the sequence and the number of steps.
    """
    sequence = []
    steps = 0
    n = start
    while n != 1 and steps < max_steps:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2  # Even: contraction
        else:
            n = 3 * n + 1  # Odd: expansion
        steps += 1
    sequence.append(1)  # Add the final 1
    return sequence, steps

# Generate sequences for a range of starting numbers
start_numbers = range(2, 21, 2)  # Start with even numbers for simplicity
results = {n: collatz_even_odd_convergence(n) for n in start_numbers}

# Prepare data for visualization
convergence_steps = [results[n][1] for n in start_numbers]

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(start_numbers, convergence_steps, color='blue', alpha=0.7)
plt.title("Collatz Convergence: Steps to Reach 1", fontsize=14)
plt.xlabel("Starting Number (Even)")
plt.ylabel("Number of Steps to 1")
plt.grid(axis='y')
plt.show()

# Display sequences for analysis
results