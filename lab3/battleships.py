# For beginners, all code in a single file without functions
board_size = 10
valid_orientations = ['horizontal', 'vertical']

###################################################################

# Exercise 1: Basic Conditional Statements
x, y = 5, 8

# TODO : 1. Check if coordinates are within the valid range
# Add you code of TODO 1 here

if 0 <= x < board_size and 0 <= y < board_size:
    print(f"Coordinates ({x}, {y}) are valid: True")
else:
    print(f"Coordinates ({x}, {y}) are valid: False")

# print(f"Coordinates ({x}, {y}) are valid: {0 <= x < board_size and 0 <= y < board_size}")

# One more example
x, y = 10, -1

if 0 <= x < board_size and 0 <= y < board_size:
    print(f"Coordinates ({x}, {y}) are valid: True")
else:
    print(f"Coordinates ({x}, {y}) are valid: False")

# TODO : 2. Check if coordinates are within the valid range
# Copy your code of TODO 1 here to test on x, y = 10, -1

###################################################################

# Exercise 2: Conditional with Logical Operators
x, y, orientation = 4, 6, 'horizontal'


# TODO : 3. Validate user input for coordinates and orientation
# Add you code of TODO 3 here

# valid = 0 <= x < board_size and 0 <= y < board_size and orientation in valid_orientations

if 0 <= x < board_size and 0 <= y < board_size and orientation in valid_orientations:
    valid = True
else:
    valid = False
print(f"Input ({x}, {y}, {orientation}) is valid: {valid}")

# One more example
x, y, orientation = 11, 3, 'diagonal'

if 0 <= x < board_size and 0 <= y < board_size and orientation in valid_orientations:
    valid = True
else:
    valid = False
print(f"Input ({x}, {y}, {orientation}) is valid: {valid}")

# TODO : 4. Validate user input for coordinates and orientation
# Copy your code of TODO 3 here to test on x, y, orientation = 11, 3, 'diagonal'


###################################################################

# Exercise 3: Nested Conditionals
x, y, ship_length, orientation = 3, 5, 4, 'horizontal'
# TODO : 5. Validate the placement of a ship
# Add you code of TODO 5 here
# One more example

valid = True
if orientation == 'horizontal':
    x_end = x + ship_length - 1
    y_end = y
elif orientation == 'vertical':
    x_end = x
    y_end = y + ship_length - 1
else:
    valid = False

if not (0 <= x < board_size and 0 <= y < board_size and 0 <= x_end < board_size and 0 <= y_end < board_size):
    valid = False
    
print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: {valid}")

x, y, ship_length, orientation = 7, 7, 4, 'vertical'
# TODO : 6. Validate the placement of a ship
# Copy your code of TODO 5 here to test on x, y, ship_length, orientation = 7, 7, 4, 'vertical'

valid = True
if orientation == 'horizontal':
    x_end = x + ship_length - 1
    y_end = y
elif orientation == 'vertical':
    x_end = x
    y_end = y + ship_length - 1
else:
    valid = False

if not (0 <= x < board_size and 0 <= y < board_size and 0 <= x_end < board_size and 0 <= y_end < board_size):
    valid = False
    
print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: {valid}")

###################################################################
