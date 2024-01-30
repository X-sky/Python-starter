from random import choice


def get_random_step(distance=[0, 1, 2, 3, 4]):
    """Determine the direction and distance for each step"""
    direction = choice([-1, 1])
    return direction * choice(distance)


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction
            x_step = get_random_step()
            y_step = get_random_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            # calculate the next x and y values
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
