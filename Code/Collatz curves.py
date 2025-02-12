import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d

# Define a function to generate a helical spiral with smooth curves
def generate_smooth_helix(start_num, max_layer, num_points=100):
    theta = np.linspace(0, 2 * np.pi * max_layer, num_points)
    z = np.linspace(0, max_layer, num_points)
    r = 5  # Constant radius for simplicity
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Map numbers onto the helix
    indices = np.linspace(0, num_points - 1, max_layer).astype(int)
    points_x = x[indices]
    points_y = y[indices]
    points_z = z[indices]
    numbers = [(start_num * (3 ** i)) % 9 + 1 for i in range(max_layer)]  # Simulate Collatz-esque behavior
    
    # Interpolate smooth curves
    interp_fn_x = interp1d(range(len(points_x)), points_x, kind='cubic')
    interp_fn_y = interp1d(range(len(points_y)), points_y, kind='cubic')
    interp_fn_z = interp1d(range(len(points_z)), points_z, kind='cubic')
    fine_t = np.linspace(0, len(points_x) - 1, num_points)
    
    smooth_x = interp_fn_x(fine_t)
    smooth_y = interp_fn_y(fine_t)
    smooth_z = interp_fn_z(fine_t)
    
    return smooth_x, smooth_y, smooth_z, points_x, points_y, points_z, numbers

# Parameters for the helix
max_layer = 10  # Number of layers
num_starts = 10  # Number of starting points
colors = plt.cm.tab10(np.linspace(0, 1, num_starts))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Collatz Helix Spiral with Smooth Curves")

for start in range(1, num_starts + 1):
    smooth_x, smooth_y, smooth_z, points_x, points_y, points_z, numbers = generate_smooth_helix(start, max_layer)
    
    # Plot the smooth curve
    ax.plot(smooth_x, smooth_y, smooth_z, color=colors[start - 1], label=f"Start {start}")
    
    # Annotate the key points (numbers)
    for px, py, pz, num in zip(points_x, points_y, points_z, numbers):
        ax.text(px, py, pz, str(num), fontsize=8, color='black')

# Set axis labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

plt.show()