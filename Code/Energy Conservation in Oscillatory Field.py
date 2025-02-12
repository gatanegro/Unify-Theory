# Initialize energy storage
total_energy_history = []

for t in range(T):
    for i in range(1, len(x)-1):
        pressure_gradient = (p[i+1] - p[i-1]) / (2 * dx)
        nonlinear_term = g_nonlinear * u[i] * (u[i+1] - u[i-1]) / (2 * dx)
        dissipation_term = nu * (u[i+1] - 2*u[i] + u[i-1]) / (dx**2)
        
        u_next[i] = (2 * u[i] - u_prev[i] +
                     dt * (-lambda_restoring * u[i] - pressure_gradient + nonlinear_term + dissipation_term))
        
        p[i] = lambda_restoring * u_next[i]**2 / 2

    # Energy calculation
    kinetic_energy = np.sum(0.5 * u_next**2)
    potential_energy = np.sum(lambda_restoring * u_next**2 / 2)
    dissipation_energy = nu * np.sum((u_next[1:] - u_next[:-1])**2) / dx

    total_energy = kinetic_energy + potential_energy - dissipation_energy
    total_energy_history.append(total_energy)

    u_prev, u = u, u_next.copy()

# Plot energy dynamics
plt.figure(figsize=(8, 6))
plt.plot(range(T), total_energy_history, label="Total Energy")
plt.title("Energy Conservation in Oscillatory Field")
plt.xlabel("Time Step")
plt.ylabel("Energy")
plt.legend()
plt.show()