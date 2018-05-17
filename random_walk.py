from random import choice

# a class to define randomwalk
class RandomWalk():
    """A class to generate random walks."""
       
    def __init__(self, num_points=5000):
        """initialize attributes of a walk."""
        self.num_points = num_points

        #all walks start at (0, 0). 
        self.x_values = [0]
        self.y_values = [0]
      
    def fill_walk(self):
        """Calculate all the points in the walk."""
    # Keep taking steps until the walk reaches the desired length. while len(self.x_values) < self.num_points:
        while len(self.x_values) < self.num_points:
            #decide which direction to go and how far
            x_direction = choice([1, -1])
            x_distance = choice ([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance 
            #these actions work by multiplying the x and y axis by a positive
            #or negative vaulue, allowing their to be a random distance and directoin

            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)