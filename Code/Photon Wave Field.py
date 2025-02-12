import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the simulation
grid_size = 200  # Size of the grid (NxN)
time_steps = 200  # Number of time steps
dx = 0.1  # Grid spacing
dt = 0.01  # Time step size
c = 1.0  # Speed of wave propagation

# Initialize the wave field (E-field)
wave_field = np.zeros((grid_size, grid_size))
wave_velocity = np.zeros((grid_size, grid_size))

# Create initial wave sources (photon-like oscillations)
sources = [
    (grid_size // 4, grid_size // 4),  # Source 1 position
    (3 * grid_size // 4, 3 * grid_size // 4),  # Source 2 position
    (grid_size // 2, grid_size // 2)  # Source 3 position
]
source_frequency = [1.0, 0.8, 1.2]  # Frequencies of the sources

# Time-dependent source term
def add_sources(wave_field, t):
    for (x, y), freq in zip(sources, source_frequency):
        wave_field[x, y] += np.sin(2 * np.pi * freq * t)

# Update function for the wave equation
def update_wave(wave_field, wave_velocity, dt, dx, c):
    laplacian = (
        np.roll(wave_field, 1, axis=0) + np.roll(wave_field, -1, axis=0) +
        np.roll(wave_field, 1, axis=1) + np.roll(wave_field, -1, axis=1) -
        4 * wave_field
    ) / dx**2

    wave_velocity += c**2 * laplacian * dt
    wave_field += wave_velocity * dt
    return wave_field, wave_velocity

# Initialize plot
fig, ax = plt.subplots()
im = ax.imshow(wave_field, cmap='viridis', interpolation='bilinear', vmin=-1, vmax=1)
ax.set_title("Photon Wave Field")

# Animation update function
def animate(t):
    global wave_field, wave_velocity
    add_sources(wave_field, t * dt)
    wave_field, wave_velocity = update_wave(wave_field, wave_velocity, dt, dx, c)
    im.set_data(wave_field)
    return [im]

# Run animation
ani = FuncAnimation(fig, animate, frames=time_steps, interval=50, blit=True)
plt.show()