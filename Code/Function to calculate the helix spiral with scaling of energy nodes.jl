# Function to calculate the helix spiral with scaling of energy nodes
function [x, y, z, labels] = collatz_helix_energy(start, max_steps)
  x = [];
  y = [];
  z = [];
  labels = {};
  current_number = start;
  step = 0;
  octave = 0;

  while current_number != 1 && step < max_steps
    # Calculate Collatz transformation
    if mod(current_number, 2) == 0
      next_number = current_number / 2;
    else
      next_number = 3 * current_number + 1;
    endif

    # Calculate helix position
    angle = (current_number % 9) * (2 * pi / 9);  # Harmonic node angle
    radius = octave + 1;  # Current field radius
    z_pos = step;  # Vertical position
    x_pos = radius * cos(angle);
    y_pos = radius * sin(angle);

    # Append current point
    x = [x, x_pos];
    y = [y, y_pos];
    z = [z, z_pos];
    labels = [labels, num2str(current_number)];  # Label with current energy node

    # Update for next step
    current_number = next_number;
    step += 1;

    # Move to next octave if number exceeds field size
    if current_number > 9
      octave += 1;
    endif
  endwhile
endfunction

# Main script: Generate the helix spiral for numbers 1 to 10
figure;
hold on;

for start = 1:10
  [x, y, z, labels] = collatz_helix_energy(start, 100);  # Max steps = 100
  plot3(x, y, z, '-o', 'LineWidth', 1.5);  # Connect points
  for i = 1:length(x)
    text(x(i), y(i), z(i), labels{i}, "fontsize", 10);  # Label points
  endfor
endfor

# Format plot
title("Collatz Helix Spiral with Energy Scaling");
xlabel("X-axis");
ylabel("Y-axis");
zlabel("Z-axis");
grid on;
hold off;