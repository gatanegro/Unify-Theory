import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 100           # Length of the spatial domain
T = 200           # Total time steps
dx = 1.0          # Spatial step size
dt = 0.1          # Time step size
c = 1.0           # Wave speed

# Initialize fields
x = np.arange(0, L, dx)
u = np.zeros_like(x)
u_prev = np.zeros_like(x)
u_next = np.zeros_like(x)

# Initial condition: localized wave packet
u[int(L/2 - 5):int(L/2 + 5)] = np.sin(np.linspace(0, np.pi, 10))

# Threshold for node detection
threshold = 0.5
nodes = []

# Store wave evolution for visualization
wave_history = []

# Time evolution
for t in range(T):
    for i in range(1, len(x)-1):
        u_next[i] = 2*u[i] - u_prev[i] + c**2 * (dt/dx)**2 * (u[i+1] - 2*u[i] + u[i-1])

    # Detect nodes
    node_indices = np.where(np.abs(u) > threshold)[0]
    nodes.append(node_indices)
    
    # Update
    u_prev, u = u, u_next.copy()
    wave_history.append(u.copy())

# Visualize wave evolution
wave_history = np.array(wave_history)
plt.figure(figsize=(12, 6))
plt.imshow(wave_history.T, aspect='auto', cmap='viridis', extent=[0, T*dt, 0, L])
plt.colorbar(label="Wave Amplitude")
plt.title("Wave Evolution in Oscillatory Field")
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()