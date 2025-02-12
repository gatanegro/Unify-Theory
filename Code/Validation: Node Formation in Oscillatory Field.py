import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 100          # Length of domain
T = 200          # Time steps
dx = 1.0         # Spatial step size
dt = 0.05        # Time step size
nu = 0.02        # Dissipation coefficient
lambda_restoring = 0.3
g_nonlinear = 0.05

# Fields
x = np.linspace(0, L, int(L/dx))
u = np.zeros_like(x)
u_prev = np.zeros_like(x)
u_next = np.zeros_like(x)
p = np.zeros_like(x)

# Initial condition: Oscillatory wave packet
u[int(L/2 - 5):int(L/2 + 5)] = np.sin(np.linspace(0, np.pi, 10))

wave_history = []

# Time evolution
for t in range(T):
    for i in range(1, len(x)-1):
        pressure_gradient = (p[i+1] - p[i-1]) / (2 * dx)
        nonlinear_term = g_nonlinear * u[i] * (u[i+1] - u[i-1]) / (2 * dx)
        dissipation_term = nu * (u[i+1] - 2*u[i] + u[i-1]) / (dx**2)
        
        u_next[i] = (2 * u[i] - u_prev[i] +
                     dt * (-lambda_restoring * u[i] - pressure_gradient + nonlinear_term + dissipation_term))
        
        p[i] = lambda_restoring * u_next[i]**2 / 2

    u_prev, u = u, u_next.copy()
    wave_history.append(u.copy())

wave_history = np.array(wave_history)

# Visualize wave evolution
plt.imshow(wave_history.T, aspect='auto', cmap='viridis', extent=[0, T*dt, 0, L])
plt.colorbar(label="Wave Amplitude")
plt.title("Validation: Node Formation in Oscillatory Field")
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()