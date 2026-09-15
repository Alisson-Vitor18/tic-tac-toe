def valid_move(board, row, column):
    if not board[row][column]:
        return True
    return False

def full_board(board):
    for row in board:
        if not all(row):
            return False
    return True

def check_win(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j]:
            return board[0][j]
    return None
