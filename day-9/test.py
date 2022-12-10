import math

# Open the input file and read the lines
f = open('day-9/input.txt', 'r')
lines = f.read().split('\n')

# Set the starting position of the snake
start_point = (0, 0)
head_pos = [0, 0]
tail_pos = [0, 0]

tail_positions = set()
tail_positions.add(start_point)

# Define a mapping from direction to movement
movement_map = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

# Iterate over the lines in the input file
for line in lines:
    # Split the line into the direction and distance
    direction, distance = line.split(' ')
    distance = int(distance)

    # Get the movement corresponding to the direction
    dx, dy = movement_map[direction]

    # Iterate over the distance in the specified direction
    for _ in range(distance):
        # Update the position of the head
        head_pos[0] += dx
        head_pos[1] += dy

        # Check if the tail needs to move
        head_tail_distance = math.sqrt((head_pos[0] - tail_pos[0]) ** 2 + (head_pos[1] - tail_pos[1]) ** 2)
        if head_tail_distance > 1:
          # Update the position of the tail
          tail_pos[0] += dx
          tail_pos[1] += dy

          # Increment the number of tail movements
          tail_positions.add((tail_pos[0], tail_pos[1]))

# Print the final number of tail movements
print(len(tail_positions))
