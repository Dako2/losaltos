import json
import time
from threading import Thread
from collections import deque

# Simulated motor control logic
class MotorControl:
    def __init__(self):
        self.angle_buffer = deque()
        self.current_angle = 0
        self.is_running = True

    def add_angle(self, angle):
        # Add angle to the buffer
        self.angle_buffer.append(angle)

    def execute_angle(self):
        # Simulate executing the angle on the motor
        while self.is_running:
            if self.angle_buffer:
                self.current_angle = self.angle_buffer.popleft()
                # Simulate motor execution
                print(f"Executing angle: {self.current_angle}")
            time.sleep(1)  # Simulate time delay between executions

    def start_execution(self):
        # Start the execution in a separate thread
        self.execution_thread = Thread(target=self.execute_angle)
        self.execution_thread.start()

    def stop_execution(self):
        # Stop the execution loop and wait for the thread to finish
        self.is_running = False
        self.execution_thread.join()

# Function to parse angle data and add it to the motor control buffer
def parse_angle_data(message, motor_control):
    angles = json.loads(message)
    x_scaled = float(angles['x']) / 3.1415926 * 4096
    motor_control.add_angle(x_scaled)

# Example usage
motor_control = MotorControl()
motor_control.start_execution()

# Simulate receiving messages
messages = ['{"x": 1.92, "y": 2.83}', '{"x": 2, "y": 2.885}', '{"x": 2.055, "y": 3.01}', '{"x": 2.055, "y": 3.12}']
for msg in messages:
    parse_angle_data(msg, motor_control)
    time.sleep(0.5)  # Simulate time delay between receiving messages

# Stop the motor execution after some time
time.sleep(5)
motor_control.stop_execution()
