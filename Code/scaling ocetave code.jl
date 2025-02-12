# Function to calculate Collatz scaling rates
function result = collatz_scaling_rates(start, max_steps)
  current_number = start;
  max_value = start;
  steps = 0;
  octave_transitions = 0;
  harmonic_loop = [1, 4, 2, 1];  # Known loop
  visited = [];  # Track visited numbers
  
  # Iterate through Collatz sequence
  while current_number != 1 && steps < max_steps
    # Stop if we enter the loop
    if ismember(current_number, harmonic_loop) && ismember(current_number, visited)
      break;
    endif
    
    visited = [visited, current_number];  # Track visited numbers
    steps += 1;  # Increment step count
    max_value = max(max_value, current_number);  # Track max value
    
    # Collatz rule
    if mod(current_number, 2) == 0
      current_number = current_number / 2;
    else
      current_number = 3 * current_number + 1;
    endif
    
    # Track octave transitions
    if current_number > 9
      octave_transitions += 1;
    endif
  endwhile
  
  # Calculate scaling rates
  expansion_rate = max_value / start;
  contraction_rate = steps / start;
  octave_rate = octave_transitions / steps;
  
  # Return results as a struct
  result = struct(
    "Starting_Number", start,
    "Expansion_Rate", expansion_rate,
    "Contraction_Rate", contraction_rate,
    "Octave_Scaling_Rate", octave_rate,
    "Max_Value", max_value,
    "Steps", steps,
    "Octave_Transitions", octave_transitions
  );
endfunction

# Main script to calculate rates for numbers 1 to 50
results = [];
for start = 1:50
  rates = collatz_scaling_rates(start, 100);  # Max steps set to 100
  results = [results; struct2cell(rates)'];
endfor

# Convert results to a matrix and display
results_matrix = cell2mat(results);
headers = {
  "Starting Number", 
  "Expansion Rate", 
  "Contraction Rate", 
  "Octave Scaling Rate", 
  "Max Value", 
  "Steps", 
  "Octave Transitions"
};

# Display the results in a table format
disp(headers);
disp(results_matrix);

# Optionally, save to a CSV file for further analysis
csvwrite("collatz_scaling_rates.csv", results_matrix);