import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 100          # Length of spatial domain
T = 200          # Total time steps
dx = 1.0         # Spatial step size
dt = 0.05        # Time step size
nu = 0.02        # Dissipation coefficient
lambda_restoring = 0.3
g_nonlinear = 0.05

# Initialize fields
x = np.linspace(0, L, int(L/dx))
u = np.zeros_like(x)         # Velocity field
u_prev = np.zeros_like(x)    # Previous velocity field
u_next = np.zeros_like(x)    # Next velocity field
p = np.zeros_like(x)         # Pressure field

# Initial condition: Localized wave packet
u[int(L/2 - 5):int(L/2 + 5)] = np.sin(np.linspace(0, np.pi, 10))

# Simulation storage
wave_history = []

# Time evolution
for t in range(T):
    for i in range(1, len(x)-1):
        # Pressure gradient
        pressure_gradient = (p[i+1] - p[i-1]) / (2 * dx)
        # Nonlinear interaction term
        nonlinear_term = g_nonlinear * u[i] * (u[i+1] - u[i-1]) / (2 * dx)
        # Dissipation term
        dissipation_term = nu * (u[i+1] - 2*u[i] + u[i-1]) / (dx**2)
        
        # Update velocity field
        u_next[i] = (2 * u[i] - u_prev[i] +
                     dt * (-lambda_restoring * u[i] - pressure_gradient + nonlinear_term + dissipation_term))

        # Update pressure
        p[i] = lambda_restoring * u_next[i]**2 / 2

    # Update for next step
    u_prev, u = u, u_next.copy()
    wave_history.append(u.copy())

# Convert wave history to numpy array
wave_history = np.array(wave_history)

# Visualize wave evolution
plt.figure(figsize=(12, 6))
plt.imshow(wave_history.T, aspect='auto', cmap='viridis', extent=[0, T*dt, 0, L])
plt.colorbar(label="Wave Amplitude")
plt.title("Node Formation in Oscillatory Field (Navier-Stokes Framework)")
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()
