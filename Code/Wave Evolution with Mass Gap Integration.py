
# Parameters for fluid-inspired dynamics
rho = 1.0
gamma = 1.4
lambda_restoring = 0.5
g_nonlinear = 0.05
nu = 0.02
E_gap = 0.5

u = np.zeros_like(x)
u_prev = np.zeros_like(x)
u_next = np.zeros_like(x)
p = np.zeros_like(x)

# Initial condition: localized wave packet
u[int(L/2 - 5):int(L/2 + 5)] = np.sin(np.linspace(0, np.pi, 10))

wave_history_mass_gap = []
energy_history = []

for t in range(T):
    for i in range(1, len(x)-1):
        pressure_gradient = (p[i+1] - p[i-1]) / (2 * dx)
        nonlinear_term = g_nonlinear * u[i] * (u[i+1] - u[i-1]) / (2 * dx)
        dissipation_term = nu * (u[i+1] - 2*u[i] + u[i-1]) / (dx**2)
        u_next[i] = (2 * u[i] - u_prev[i] +
                     dt * (-pressure_gradient * lambda_restoring / rho - nonlinear_term + dissipation_term))
        p[i] = gamma * rho * u_next[i]**2 / 2
    total_energy = np.sum(0.5 * rho * u_next**2 + p / (gamma - 1))
    energy_history.append(total_energy)
    u_prev, u = u, u_next.copy()
    wave_history_mass_gap.append(u.copy())

wave_history_mass_gap = np.array(wave_history_mass_gap)
plt.figure(figsize=(12, 6))
plt.imshow(wave_history_mass_gap.T, aspect='auto', cmap='viridis', extent=[0, T*dt, 0, L])
plt.colorbar(label="Velocity Field (u)")
plt.title("Wave Evolution with Mass Gap Integration")
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()
