% Simulation of the Boomerang Node in THE FIELD

% Parameters
L = 10;         % Spatial domain length (space amplitude)
T = 10;         % Temporal domain length (time longitude)
Nx = 200;       % Number of spatial points
Nt = 200;       % Number of temporal points
k = 2 * pi / 5; % Wave number (spatial frequency)
omega = 2 * pi / T; % Angular frequency (temporal oscillations)

x = linspace(0, L, Nx); % Space grid
t = linspace(0, T, Nt); % Time grid
[X, T_grid] = meshgrid(x, t); % Create 2D grid for space and time

% Define the boomerang energy node as a localized oscillator
A = exp(-((X - L/2).^2) / (2 * (L/10)^2)); % Amplitude envelope (localized)
E_boomerang = A .* sin(k * X - omega * T_grid); % Energy density of the boomerang

% Define the background FIELD oscillation
E_field = 0.5 * sin(k * X + omega * T_grid); % Background oscillatory field

% Total FIELD energy
E_total = E_boomerang + E_field;

% Plot the energy redistribution over space and time
figure;
surf(x, t, E_total, 'EdgeColor', 'none');
view(2);
colorbar;
colormap(jet);
title('Energy Density in THE FIELD with Boomerang Node');
xlabel('Space (Amplitude)');
ylabel('Time (Longitude)');

% Highlight the energy node behavior dynamically
figure;
for i = 1:10:Nt
    plot(x, E_total(i, :), 'LineWidth', 1.5);
    ylim([-1.5, 1.5]);
    title(sprintf('Energy Profile at Time %.2f', t(i)));
    xlabel('Space (Amplitude)');
    ylabel('Energy Density');
    pause(0.1);
end

import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10          # Spatial domain length (space amplitude)
T = 10          # Temporal domain length (time longitude)
Nx = 200        # Number of spatial points
Nt = 200        # Number of temporal points
k = 2 * np.pi / 5  # Wave number (spatial frequency)
omega = 2 * np.pi / T  # Angular frequency (temporal oscillations)

x = np.linspace(0, L, Nx)  # Space grid
t = np.linspace(0, T, Nt)  # Time grid
X, T_grid = np.meshgrid(x, t)  # Create 2D grid for space and time

# Define the boomerang energy node as a localized oscillator
A = np.exp(-((X - L / 2) ** 2) / (2 * (L / 10) ** 2))  # Amplitude envelope (localized)
E_boomerang = A * np.sin(k * X - omega * T_grid)  # Energy density of the boomerang

# Define the background FIELD oscillation
E_field = 0.5 * np.sin(k * X + omega * T_grid)  # Background oscillatory field

# Total FIELD energy
E_total = E_boomerang + E_field

# Plot the energy redistribution over space and time (surface plot)
plt.figure(figsize=(10, 6))
plt.imshow(E_total, extent=[0, L, 0, T], aspect='auto', origin='lower', cmap='jet')
plt.colorbar(label='Energy Density')
plt.title('Energy Density in THE FIELD with Boomerang Node')
plt.xlabel('Space (Amplitude)')
plt.ylabel('Time (Longitude)')
plt.show()

# Dynamic 2D plot of energy node behavior over time
for i in range(0, Nt, 10):  # Every 10th time step
    plt.figure(figsize=(8, 4))
    plt.plot(x, E_total[i, :], linewidth=1.5)
    plt.ylim([-1.5, 1.5])
    plt.title(f'Energy Profile at Time {t[i]:.2f}')
    plt.xlabel('Space (Amplitude)')
    plt.ylabel('Energy Density')
    plt.grid()
    plt.show()