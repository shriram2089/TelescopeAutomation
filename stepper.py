from machine import Pin
import time

class StepperMotor:
    def __init__(self, step_pin, dir_pin):
        self.step_pin = Pin(step_pin, Pin.OUT)
        self.dir_pin = Pin(dir_pin, Pin.OUT)

    def step(self, steps=1, direction='cw', delay=0.001):
        if direction == 'ccw':
            self.dir_pin.value(1)  # Set direction to counterclockwise
        else:
            self.dir_pin.value(0)  # Set direction to clockwise
        for _ in range(steps):
            self.step_pin.on()  # Generate a step pulse
            time.sleep(delay)  # Wait
            self.step_pin.off()  # Turn off step pulse
            time.sleep(delay)  # Wait

# Define pin numbers
STEP_PIN = 4
DIR_PIN = 13

# Create a stepper motor instance
motor = StepperMotor(STEP_PIN, DIR_PIN)

# Move the motor 200 steps clockwise
motor.step(steps=200, direction='cw')

# Move the motor 200 steps counterclockwise
motor.step(steps=200, direction='ccw')
