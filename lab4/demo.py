board_size = 10

# TODO : 1. Initialize a board_size x board_size game board with all cells set to 0 (empty)
# Add you code of TODO 1 here
board = [[0] * board_size for _ in range(board_size)]

# TODO : 2.While loop to repeatedly ask for valid attack coordinates
# Add you code of TODO 2 here

valid = False
while not valid:
    attack_row_str = input("Enter attack row (0-9): ")
    attack_col_str = input("Enter attack column (0-9): ")
    if not attack_row_str.isdigit() or not attack_col_str.isdigit():
        valid = False
    else:
        attack_row = int(attack_row_str)
        attack_col = int(attack_col_str)
        valid = 0 <= attack_row < board_size and 0 <= attack_col < board_size

    print(f"Coordinates ({attack_row_str}, {attack_col_str}) are valid: {valid}")
    if not valid:
        print("Please enter again")

# TODO : 3. For loop to iterate through each row and column of the board
# Add you code of TODO 3 here

board[attack_row][attack_col] = 1

for row in board:
    for col in row:
        print(col, end=" ")
    print()
