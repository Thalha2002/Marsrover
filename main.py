# Define the Command Pattern
class Command:
    def execute(self, rover):
        pass

class MoveCommand(Command):
    def execute(self, rover):
        rover.move()

class TurnLeftCommand(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRightCommand(Command):
    def execute(self, rover):
        rover.turn_right()

# Define the Mars Rover class
class MarsRover:
    def __init__(self, x, y, direction, grid, obstacles):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.obstacles = obstacles

    def move(self):
        if self.direction == 'N' and self.y < self.grid['height'] - 1:
            self.y += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'E' and self.x < self.grid['width'] - 1:
            self.x += 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def execute_commands(self, commands):
        for command in commands:
            if command == 'M':
                new_x, new_y = self.x, self.y
                if self.direction == 'N':
                    new_y += 1
                elif self.direction == 'S':
                    new_y -= 1
                elif self.direction == 'E':
                    new_x += 1
                elif self.direction == 'W':
                    new_x -= 1
                
                if (
                    self.grid['width'] > new_x >= 0
                    and self.grid['height'] > new_y >= 0
                    and (new_x, new_y) not in self.obstacles
                ):
                    self.move()
            elif command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()

    def send_status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No obstacles detected."

# Initialize the grid and obstacles
grid_size = {'width': 10, 'height': 10}
obstacles = [(2, 2), (3, 5)]

# Initialize and run the Mars Rover
rover = MarsRover(0, 0, 'N', grid_size, obstacles)
commands = ['M', 'M', 'R', 'M', 'L', 'M']
rover.execute_commands(commands)
status_report = rover.send_status_report()

print(f"Final Position: {status_report}")
