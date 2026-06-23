def is_safe(board, row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]
        if previous_col == col or abs(previous_col - col) == abs(previous_row - row):
            return False
    return True


def solve(board, row=0):
    size = len(board)
    if row == size:
        return True

    for col in range(size):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
            board[row] = -1

    return False


def display(board):
    for queen_col in board:
        print(" ".join("Q" if col == queen_col else "." for col in range(len(board))))


if __name__ == "__main__":
    board = [-1] * 4
    if solve(board):
        print("Solution for 4-Queens:")
        display(board)
