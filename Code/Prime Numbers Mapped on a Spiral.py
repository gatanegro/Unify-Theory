# Generate prime numbers using the Sieve of Eratosthenes
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [x for x in range(limit + 1) if sieve[x]]

# Generate primes up to a limit
prime_limit = 500
primes = generate_primes(prime_limit)

# Map primes onto a spiral for symmetry visualization
def prime_spiral(primes):
    theta = [i * 2 * np.pi / 10 for i in range(len(primes))]  # Angular progression
    radius = [np.log2(p + 1) for p in primes]  # Radius based on prime magnitude
    x = [r * np.cos(t) for r, t in zip(radius, theta)]
    y = [r * np.sin(t) for r, t in zip(radius, theta)]
    return x, y

# Generate spiral coordinates for primes
x_spiral, y_spiral = prime_spiral(primes)

# Plot the prime spiral
plt.figure(figsize=(10, 8))
plt.scatter(x_spiral, y_spiral, c="blue", label="Primes", s=30)
plt.title("Prime Numbers Mapped on a Spiral", fontsize=16)
plt.xlabel("X Coordinate", fontsize=14)
plt.ylabel("Y Coordinate", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.show()