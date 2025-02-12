from mpl_toolkits.mplot3d import Axes3D

# Define a function to plot Collatz sequences as a 3D spiral
def plot_collatz_spiral_3D(collatz_data, title="Collatz Sequences as 3D Spiral"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    for key, seq in collatz_data.items():
        # Generate 3D coordinates: step (z), sequence value (radius), and angle (theta)
        z = np.arange(len(seq))  # Steps as the height
        r = np.array(seq)  # Node values as radius
        theta = 2 * np.pi * z / len(seq)  # Spiral angle (proportional to step)
        
        # Convert polar coordinates (r, theta) to Cartesian (x, y)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        ax.plot(x, y, z, label=f"Start: {key}")

    ax.set_title(title)
    ax.set_xlabel("X (Energy Field)")
    ax.set_ylabel("Y (Energy Field)")
    ax.set_zlabel("Z (Step / Time)")
    ax.legend()
    plt.show()

# Plot Collatz sequences as a 3D spiral
plot_collatz_spiral_3D(collatz_data, title="Collatz Sequences Visualized as a 3D Spiral")
