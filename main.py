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

# Get user input for grid size and obstacles
width = int(input("Enter grid width: "))
height = int(input("Enter grid height: "))
grid_size = {'width': width, 'height': height}

obstacles = []
num_obstacles = int(input("Enter the number of obstacles: "))
for i in range(num_obstacles):
    obstacle_x = int(input(f"Enter x-coordinate of obstacle {i + 1}: "))
    obstacle_y = int(input(f"Enter y-coordinate of obstacle {i + 1}: "))
    obstacles.append((obstacle_x, obstacle_y))

# Get user input for initial position and direction
initial_x = int(input("Enter initial x-coordinate: "))
initial_y = int(input("Enter initial y-coordinate: "))
initial_direction = input("Enter initial direction (N/S/E/W): ")

# Get user input for commands
commands = input("Enter commands (e.g., MMLRMM): ")

# Initialize and run the Mars Rover
rover = MarsRover(initial_x, initial_y, initial_direction, grid_size, obstacles)
rover.execute_commands(commands)
status_report = rover.send_status_report()

print(f"Final Position: {status_report}")# Define the Command Pattern
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

# Get user input for grid size and obstacles
width = int(input("Enter grid width: "))
height = int(input("Enter grid height: "))
grid_size = {'width': width, 'height': height}

obstacles = []
num_obstacles = int(input("Enter the number of obstacles: "))
for i in range(num_obstacles):
    obstacle_x = int(input(f"Enter x-coordinate of obstacle {i + 1}: "))
    obstacle_y = int(input(f"Enter y-coordinate of obstacle {i + 1}: "))
    obstacles.append((obstacle_x, obstacle_y))

# Get user input for initial position and direction
initial_x = int(input("Enter initial x-coordinate: "))
initial_y = int(input("Enter initial y-coordinate: "))
initial_direction = input("Enter initial direction (N/S/E/W): ")

# Get user input for commands
commands = input("Enter commands (e.g., MMLRMM): ")

# Initialize and run the Mars Rover
rover = MarsRover(initial_x, initial_y, initial_direction, grid_size, obstacles)
rover.execute_commands(commands)
status_report = rover.send_status_report()

print(f"Final Position: {status_report}")# Define the Command Pattern
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

# Get user input for grid size and obstacles
width = int(input("Enter grid width: "))
height = int(input("Enter grid height: "))
grid_size = {'width': width, 'height': height}

obstacles = []
num_obstacles = int(input("Enter the number of obstacles: "))
for i in range(num_obstacles):
    obstacle_x = int(input(f"Enter x-coordinate of obstacle {i + 1}: "))
    obstacle_y = int(input(f"Enter y-coordinate of obstacle {i + 1}: "))
    obstacles.append((obstacle_x, obstacle_y))

# Get user input for initial position and direction
initial_x = int(input("Enter initial x-coordinate: "))
initial_y = int(input("Enter initial y-coordinate: "))
initial_direction = input("Enter initial direction (N/S/E/W): ")

# Get user input for commands
commands = input("Enter commands (e.g., MMLRMM): ")

# Initialize and run the Mars Rover
rover = MarsRover(initial_x, initial_y, initial_direction, grid_size, obstacles)
rover.execute_commands(commands)
status_report = rover.send_status_report()

print(f"Final Position: {status_report}")
