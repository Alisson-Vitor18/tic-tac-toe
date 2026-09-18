class TicTacToe:
    def __init__(self):
        self.buttons = [
            [None,None, None],
            [None,None, None],
            [None,None, None],
        ]

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