#!/usr/bin/python3

def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Return True if there's a winning line on the board."""
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[1][1] != " " and (
       (board[0][0] == board[1][1] == board[2][2]) or
       (board[0][2] == board[1][1] == board[2][0])
    ):
        return True

    return False

def board_full(board):
    """Return True if all cells are filled (no more moves)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input validation for row
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in (0, 1, 2):
                    raise ValueError
                break
            except ValueError:
                print("Invalid row. Please enter 0, 1, or 2.")

        # Input validation for column
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in (0, 1, 2):
                    raise ValueError
                break
            except ValueError:
                print("Invalid column. Please enter 0, 1, or 2.")

        # Check if the chosen cell is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the mark
        board[row][col] = player

        # Check for a win
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for a tie
        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
