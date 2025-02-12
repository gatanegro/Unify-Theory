# Enhance the helix spiral visualization to show gradients and nodes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the gradients and nodes with enhanced visualization
for i in range(1, len(helix_data)):
    x_prev, y_prev, z_prev, h_prev = helix_data[i - 1]
    x, y, z, h = helix_data[i]
    
    # Distinguish gradients and nodes
    if h_prev == h:  # Node: Same harmonic value
        ax.scatter(x, y, z, c='blue', s=h*8, alpha=0.7)  # Nodes as blue points
    else:  # Gradient: Transition between nodes
        ax.plot([x_prev, x], [y_prev, y], [z_prev, z], c='orange', alpha=0.5)  # Gradients as orange lines

# Highlight specific integer nodes
key_numbers = [1, 2, 3, 4, 5, 8, 9]
for x, y, z, h in helix_data:
    if h in key_numbers:
        ax.text(x, y, z, str(h), fontsize=8, ha='center', va='center', color='red')

# Styling the plot
ax.set_title("Enhanced Collatz Helix: Nodes and Gradients (1 to 50)", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()