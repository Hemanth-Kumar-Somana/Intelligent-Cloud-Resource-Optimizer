import zmq
import json
import time

# Setup ZMQ context and publisher socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.1:5555")

# Wait to ensure subscriber is ready
time.sleep(1)

# Build the message to send
message = {
    "sender": "user",
    "recipient": "Julia",
    "content": "Hello Julia! Can you describe your current task?"
}

# Send the message as JSON string
socket.send_string(json.dumps(message))
print("✅ Sent message to Julia.")
