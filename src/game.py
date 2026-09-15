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
        winning_cells = [(0, 0), (1, 1), (2, 2)]
        return board[0][0], winning_cells

    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        winning_cells = [(0, 2), (1, 1), (2, 0)]
        return board[0][2], winning_cells

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            winning_cells = [(i, 0), (i, 1), (i, 2)]
            return board[i][0], winning_cells

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j]:
            winning_cells = [(0, j), (1, j), (2, j)]
            return board[0][j], winning_cells
    return None, []

def swap_turns(state):
    if state["turn"] == "X":
        state["turn"] = "O"
    else:
        state["turn"] = "X"