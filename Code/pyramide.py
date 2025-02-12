    2. import numpy as np
       import matplotlib.pyplot as plt
       from mpl_toolkits.mplot3d import Axes3D
       
       # Pyramid dimensions (Keops Pyramid size)
       height = 146.6  # Height in meters
       base_width = 230.4  # Base width in meters
       
       # Create a 3D grid for the pyramid model
       grid_size = 100  # Grid resolution
       x = np.linspace(-base_width / 2, base_width / 2, grid_size)
       y = np.linspace(-base_width / 2, base_width / 2, grid_size)
       z = np.linspace(0, height, grid_size)
       
       X, Y, Z = np.meshgrid(x, y, z)
       
       # Energy distribution: based on distance from the apex (top of the pyramid)
       # The energy density will be modeled as a function of height (Z) with the highest at the base
       # and decreasing towards the apex.
       def energy_distribution(x, y, z, height, base_width):
           # Linear scale for the pyramid's side
           distance_to_apex = np.sqrt(x**2 + y**2)  # Horizontal distance from the apex (top)
           scaling_factor = (base_width - distance_to_apex) / base_width  # Decreases towards the apex
           energy_density = np.exp(-((z - height) / (height))**2) * scaling_factor  # Decays with height
           return energy_density
       
       # Calculate energy distribution for each point in the pyramid grid
       energy = energy_distribution(X, Y, Z, height, base_width)
       
       # Plotting the 3D energy distribution inside the pyramid
       fig = plt.figure(figsize=(12, 10))
       ax = fig.add_subplot(111, projection='3d')
       
       # Plot the energy density as a surface plot
       ax.plot_surface(X, Y, energy[:, :, grid_size // 2], cmap='hot', edgecolor='none')
       
       # Labels and title
       ax.set_xlabel('X (meters)')
       ax.set_ylabel('Y (meters)')
       ax.set_zlabel('Energy Density')
       ax.set_title('Energy Distribution Inside a Pyramid (Keops size)')
       
       plt.show()
