def detect_nodes(field, threshold=0.5):
    return np.argwhere(np.abs(field) > threshold)

def extract_node_parameters(field, node):
    x = node[0]
    amplitude = field[x]
    return {"amplitude": amplitude, "position": x}

def recreate_node(field, node_params, target_position):
    x_target = target_position
    amplitude = node_params["amplitude"]
    radius = 3
    for i in range(max(0, x_target-radius), min(len(field), x_target+radius)):
        field[i] += amplitude * np.sin(np.pi * np.abs(i-x_target) / radius)
    return field

# Node reproduction setup
target_position = 10
for t in range(T):
    for i in range(1, len(x)-1):
        u_next[i] = 2*u[i] - u_prev[i] + c**2 * (dt/dx)**2 * (u[i+1] - 2*u[i] + u[i-1])
    if t == 50:
        nodes = detect_nodes(u_next, threshold)
        if len(nodes) > 0:
            chosen_node = nodes[0]
            node_params = extract_node_parameters(u_next, chosen_node)
            u_next = recreate_node(u_next, node_params, target_position)
    u_prev, u = u, u_next.copy()
    wave_history.append(u.copy())