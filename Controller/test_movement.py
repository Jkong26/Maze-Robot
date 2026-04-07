# test_movement.py
# Author: Jenjira Kongpong
# Purpose: Test Detailed Movement System in Webots

from controller import Robot
from movement import move_forward, turn_left, turn_right, stop

# ----------------------------
# Configuration
# ----------------------------
TIME_STEP = 64   # Webots simulation step in ms

# ----------------------------
# Initialize Robot
# ----------------------------
robot = Robot()
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Set motors to velocity control mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# ----------------------------
# Detailed step-by-step movement test
# ----------------------------
def movement_test():
    print("Starting e-puck detailed movement test...")

    # ------------------------
    # 1. MOVE FORWARD
    # ------------------------
    print("Step 1: Moving forward")
    move_forward(left_motor, right_motor, 3.0)
    for _ in range(40):
        robot.step(TIME_STEP)

    # ------------------------
    # 2. TURN LEFT
    # ------------------------
    print("Step 2: Turning left")
    turn_left(left_motor, right_motor, 1.5)
    for _ in range(18):
        robot.step(TIME_STEP)

    # ------------------------
    # 3. RETURN TO FRONT (camera)
    # ------------------------
    print("Step 3: Returning to front")
    for step in range(18):
        turn_speed = 1.5 if step < 9 else 0.8
        turn_right(left_motor, right_motor, turn_speed)
        robot.step(TIME_STEP)

        if step == 9:
            print("Pausing for 0.3 sec")
            turn_right(left_motor, right_motor, 0.3)
            for _ in range(5):
                robot.step(TIME_STEP)
            turn_right(left_motor, right_motor, 1.5)

    # ------------------------
    # 4. TURN RIGHT
    # ------------------------
    print("Step 4: Turning right")
    turn_right(left_motor, right_motor, 1.5)
    for _ in range(18):
        robot.step(TIME_STEP)

    # ------------------------
    # 5. STOP
    # ------------------------
    print("Step 5: Stopping")
    stop(left_motor, right_motor)
    for _ in range(10):
        robot.step(TIME_STEP)

    print("Detailed Movement Test Completed.")

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    movement_test()
