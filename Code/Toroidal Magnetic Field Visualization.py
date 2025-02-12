# Fixing the indexing issue for quiver plot
import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the toroidal field visualization
theta = np.linspace(0, 2 * np.pi, 100)  # Angle around the toroid
phi = np.linspace(0, 2 * np.pi, 100)  # Angle along the toroid

# Define toroid radius parameters
R = 3  # Major radius (distance from center of hole to toroid center)
r = 1  # Minor radius (radius of the tube)

# Create meshgrid
Theta, Phi = np.meshgrid(theta, phi)

# Parametric equations for a torus
X = (R + r * np.cos(Phi)) * np.cos(Theta)
Y = (R + r * np.cos(Phi)) * np.sin(Theta)
Z = r * np.sin(Phi)

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the toroidal structure
ax.plot_surface(X, Y, Z, color='c', edgecolor='k', alpha=0.6)

# Magnetic field lines visualization (approximated as vector field on toroidal surface)
# Define vector field components (idealized toroidal field)
B_theta = -np.sin(Theta)  # Opposite directions around toroid
B_phi = np.cos(Phi)  # Field follows toroidal shape

# Sample points for quiver plot
idx = np.arange(0, 100, 10)
idy = np.arange(0, 100, 10)

# Plot vector field on toroidal surface
ax.quiver(X[idx, :][:, idy], Y[idx, :][:, idy], Z[idx, :][:, idy],
          B_theta[idx, :][:, idy], B_phi[idx, :][:, idy], np.zeros_like(B_phi[idx, :][:, idy]),
          color='r', length=0.5, normalize=True)

# Labels and aesthetics
ax.set_title("Toroidal Magnetic Field Visualization")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

plt.show()
