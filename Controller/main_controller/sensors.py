class Sensors:
    def __init__(self, robot, ps):
        self.robot = robot
        self.ps = ps

    def read(self):
        values = [p.getValue() for p in self.ps]

        # ps0 = front-right, ps7 = front-left → average for front
        # ps1 = right, ps6 = left
        front = (values[7] + values[0]) * 0.5
        left  = values[6]
        right = values[1]

        return {
            "front": front,
            "left":  left,
            "right": right
        }
