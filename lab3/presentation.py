# For beginners, all code in a single file without functions
board_size = 10
valid_orientations = ['horizontal', 'vertical']

###################################################################

# Exercise 1: Basic Conditional Statements
x, y = 5, 8

# TODO : 1. Check if coordinates are within the valid range
# Add you code of TODO 1 here

# if 0 <= x < board_size and 0 <= y < board_size:
#     print(f"Coordinates ({x}, {y}) are valid: True")
# else:
#     print(f"Coordinates ({x}, {y}) are valid: False")

valid = 0 <= x < board_size and 0 <= y < board_size
print(f"Coordinates ({x}, {y}) are valid: {valid}")

# One more example
x, y = 10, -1

# TODO : 2. Check if coordinates are within the valid range
# Copy your code of TODO 1 here to test on x, y = 10, -1

valid = 0 <= x < board_size and 0 <= y < board_size
print(f"Coordinates ({x}, {y}) are valid: {valid}")

###################################################################

# Exercise 2: Conditional with Logical Operators
x, y, orientation = 4, 6, 'horizontal'

# TODO : 3. Validate user input for coordinates and orientation
# Add you code of TODO 3 here

# if 0 <= x < board_size and 0 <= y < board_size and (orientation == "horizontal" or orientation == "vertical"):
#     print(f"Input ({x}, {y}, {orientation}) is valid: True")
# else:
#     print(f"Input ({x}, {y}, {orientation}) is valid: False")

# if 0 <= x < board_size and 0 <= y < board_size and orientation in valid_orientations:
#     print(f"Input ({x}, {y}, {orientation}) is valid: True")
# else:
#     print(f"Input ({x}, {y}, {orientation}) is valid: False")

valid = 0 <= x < board_size and 0 <= y < board_size and orientation in valid_orientations
print(f"Input ({x}, {y}, {orientation}) is valid: {valid}")

# One more example
x, y, orientation = 11, 3, 'diagonal'

# TODO : 4. Validate user input for coordinates and orientation
# Copy your code of TODO 3 here to test on x, y, orientation = 11, 3, 'diagonal'
valid = 0 <= x < board_size and 0 <= y < board_size and orientation in valid_orientations
print(f"Input ({x}, {y}, {orientation}) is valid: {valid}")


###################################################################

# Exercise 3: Nested Conditionals
x, y, ship_length, orientation = 3, 5, 4, 'horizontal'
# TODO : 5. Validate the placement of a ship
# Add you code of TODO 5 here

# valid = True

# if not (0 <= x < board_size and 0 <= y < board_size):
#     valid = False
# elif orientation not in valid_orientations:
#     valid = False

# if orientation == "horizontal":
#     x_other = x + ship_length - 1
#     y_other = y
# else:
#     x_other = x
#     y_other = y + ship_length - 1

# if not (0 <= x_other < board_size and 0 <= y_other < board_size):
#     valid = False
    
# print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: {valid}")

if orientation == "horizontal":
    if 0 <= x < board_size - ship_length + 1 and 0 <= y < board_size:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: True")
    else:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: False")
elif orientation == "vertical":
    if 0 <= x < board_size and 0 <= y < board_size - ship_length + 1:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: True")
    else:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: False")
else:
    print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: False")

# One more example
x, y, ship_length, orientation = 7, 7, 4, 'vertical'

# TODO : 6. Validate the placement of a ship
# Copy your code of TODO 5 here to test on x, y, ship_length, orientation = 7, 7, 4, 'vertical'

# valid = True

# if not (0 <= x < board_size and 0 <= y < board_size):
#     valid = False
# elif orientation not in valid_orientations:
#     valid = False

# if orientation == "horizontal":
#     x_other = x + ship_length - 1
#     y_other = y
# else:
#     x_other = x
#     y_other = y + ship_length - 1

# if not (0 <= x_other < board_size and 0 <= y_other < board_size):
#     valid = False
    
# print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: {valid}")

if orientation == "horizontal":
    if 0 <= x < board_size - ship_length + 1 and 0 <= y < board_size:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: True")
    else:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: False")
elif orientation == "vertical":
    if 0 <= x < board_size and 0 <= y < board_size - ship_length + 1:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: True")
    else:
        print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: False")
else:
    print(f"Placement ({x}, {y}, {ship_length}, {orientation}) is valid: False")

###################################################################
