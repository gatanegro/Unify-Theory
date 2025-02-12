# VR-Powered Python Math Lab Prototype
# This script sets up a WebSocket bridge between Python (math computations) and a Three.js VR environment.

import asyncio
import websockets
import json
import numpy as np
import sympy as sp

# Define a simple field function to send to VR
def compute_field(t):
    x, y = np.meshgrid(np.linspace(-5, 5, 30), np.linspace(-5, 5, 30))
    field = np.sin(x * t) * np.cos(y * t)  # Example dynamic wave field
    return field.tolist()

async def send_math_data(websocket, path):
    """Sends computed field data to the VR WebSocket connection."""
    t = 0
    while True:
        field_data = compute_field(t)
        response = json.dumps({"time": t, "field": field_data})
        await websocket.send(response)
        t += 0.1  # Increment simulation time
        await asyncio.sleep(0.1)  # Adjust refresh rate

# Run WebSocket Server
start_server = websockets.serve(send_math_data, "localhost", 8765)
print("WebSocket Server running on ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()