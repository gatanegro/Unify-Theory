# Calculate the FIELD gradient (tension) from the sine wave energy
def calculate_gradient(x, y):
    gradient = np.gradient(y, x)  # Numerical gradient of the energy wave
    return gradient

# Compute the gradient for the sine wave representation
gradient_wave = calculate_gradient(x_wave, y_wave)

# Visualize both the energy wave and its gradient (tensions)
plt.figure(figsize=(12, 8))

# Plot the energy wave
plt.subplot(2, 1, 1)
plt.plot(x_wave, y_wave, label="Energy Wave (Collatz Sequence)", color="blue")
plt.axhline(1, color="green", linestyle="--", label="Attractor (1)")
plt.scatter(x_wave[peak_index], peak_energy, color="red", label=f"Peak Energy: {peak_energy:.2f}", zorder=5)
plt.title("Energy Wave and FIELD Gradient", fontsize=16)
plt.ylabel("Energy (Amplitude)", fontsize=14)
plt.legend()
plt.grid(alpha=0.3)

# Plot the FIELD gradient (tensions)
plt.subplot(2, 1, 2)
plt.plot(x_wave, gradient_wave, label="FIELD Gradient (Tension)", color="purple")
plt.axhline(0, color="black", linestyle="--", label="Equilibrium (No Tension)")
plt.title("FIELD Gradient (Tensions)", fontsize=14)
plt.xlabel("Wave Progression (Steps)", fontsize=14)
plt.ylabel("Gradient (Tension)", fontsize=14)
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()