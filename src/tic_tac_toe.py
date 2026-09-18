class TicTacToe:
    def __init__(self):
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

        self.turn = "X"
        self.end_game = False

    def swap_turns(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"