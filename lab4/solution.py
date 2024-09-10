board_size = 10

# TODO : 1. Initialize a board_size x board_size game board with all cells set to 0 (empty)
# Add you code of TODO 1 here

board = []
for i in range(board_size):
    row = []
    for j in range(board_size):
        row.append(0)
    board.append(row)

# board = [[0] * board_size for _ in range(board_size)]

# TODO : 2.While loop to repeatedly ask for valid attack coordinates
# Add you code of TODO 2 here

valid = False
while not valid:
    # x = input("Enter attack row (0-9): ")
    # y = input("Enter attack column (0-9): ")
    # valid = True
    # # if x or y are not numbers
    # if not x.isdigit() or not y.isdigit():
    #     print("Invalid input. Please enter a number.")
    #     valid = False
    #     continue
    # x = int(x)
    # y = int(y)
    # # if x or y are out of range
    # if x < 0 or x >= board_size or y < 0 or y >= board_size:
    #     print("Invalid input. Please enter a number between 0 and 9.")
    #     valid = False

    # Another solution:
    try:
        x = int(input("Enter attack row (0-9): "))
        y = int(input("Enter attack column (0-9): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    valid = 0 <= x < board_size and 0 <= y < board_size
    if not valid:
        print("Invalid input. Please enter a number between 0 and 9.")

board[x][y] = 1

# TODO : 3. For loop to iterate through each row and column of the board
# Add you code of TODO 3 here

for i in range(board_size):
    for j in range(board_size):
        print(board[i][j], end=" ")
    print()
