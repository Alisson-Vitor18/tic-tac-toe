def valid_move(board, row, column):
    if not board[row][column]:
        return True
    return False

def full_board(board):
    for row in board:
        if not all(row):
            return False
    return True