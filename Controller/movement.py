# movement.py
# Purpose: Motor control functions for e-puck movements

MAX_SPEED = 6.28  # Default max wheel speed (rad/s)

def move_forward(left_motor, right_motor, speed=MAX_SPEED):
    """Move the robot forward."""
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

def turn_left(left_motor, right_motor, speed=MAX_SPEED):
    """Turn the robot left."""
    left_motor.setVelocity(-speed)
    right_motor.setVelocity(speed)

def turn_right(left_motor, right_motor, speed=MAX_SPEED):
    """Turn the robot right."""
    left_motor.setVelocity(speed)
    right_motor.setVelocity(-speed)

def stop(left_motor, right_motor):
    """Stop the robot."""
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
