import customtkinter as ctk
import pygame
import game as game_logic
from sound import SOUNDS_DIR
pygame.mixer.init()

click_sound = pygame.mixer.Sound(
    SOUNDS_DIR / "click_002.ogg"
)

init_sound = pygame.mixer.Sound(
    SOUNDS_DIR / "start.wav"
)

click_sound.set_volume(0.05)
init_sound.set_volume(0.1)

class TicTacToeInterface:
    def __init__(self):
        self.width = 500
        self.height = 600
        self.window = None

        self.create_window()

        self.frame = None
        self.restart_frame = None
        self.restart_button =  None
        self.title_game = None
        self.turn_message = None
        self.buttons = [
            [None,None, None],
            [None,None, None],
            [None,None, None],
        ]

    def create_window(self):
        self.window = ctk.CTk()
        self.window.geometry(
            self.__center_window()
        )
        self.window.resizable(False, False)

    def __center_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        scale = self.window._get_window_scaling()

        x = int(((screen_width - self.width) // 2) * scale)
        y = int(((screen_height - self.height) // 2) * scale)

        return f"{self.width}x{self.height}+{x}+{y}"

    def restart_game(self, game):
        click_sound.play()
        init_sound.play()

        self.restart_button.configure(
            state="disabled",
            fg_color="#6A6868",
            hover_color="#6A6868",
        )

        for row in range(3):
            for column in range(3):
                game.board[row][column]=""
                self.buttons[row][column].configure(
                    text="",
                    fg_color="white",
                    hover_color="#ECECEC"
                )
        game.turn="X"
        game.end_game=False

        self.turn_message.configure(text="Vez de jogador X")
        print("Jogo reiniciado")

    def create_restart_button(self, game):
        font = ctk.CTkFont(
            family="Segoe UI Variable Display",
            size=28,
            weight="bold"
        )

        button = ctk.CTkButton(
            self.restart_frame,
            state="disabled",
            text="Reiniciar Jogo",
            text_color="#060606",
            font=font,
            border_width=3,
            border_color="#060606",
            fg_color="#6A6868",
            hover_color="#6A6868",
            width=210,
            height=50,
            command=lambda:self.restart_game(game=game)
        )   
        button.pack()

        return button

    def button_click(self, button, row, column, game):
        if game.end_game:
            return

        if game_logic.valid_move(game.board, row, column):
            click_sound.play()
            button.configure(
                fg_color= "#E4E4E4",
                text = game.turn
            )

            game.board[row][column] = game.turn
            print(f"Jogador {game.turn} escolheu a casa {(row, column)}")

            result, winning_cells = game_logic.check_win(game.board)

            if result is not None:
                print(f"\033[30;47mFim de jogo. jogador {result} venceu!\033[0m")
                self.turn_message.configure(text=f"Jogador {result} venceu!")
                for row, column in winning_cells:
                    self.buttons[row][column].configure(
                        fg_color="#B0CEB1",
                        hover_color="#C6E0C7"
                    )
                game.end_game = True
                self.restart_button.configure(
                    state="normal",
                    fg_color="#B0CEB1",
                    hover_color="#C6E0C7"
                )
                return

            if game_logic.full_board(game.board):
                print("Fim de jogo. Empate!")
                self.turn_message.configure(text=f"Empate!")
                game.end_game = True
                self.restart_button.configure(
                    state="normal",
                    fg_color="#B0CEB1",
                    hover_color="#C6E0C7"
                )
                return

            game.swap_turns()
            self.turn_message.configure(
                text=f"Vez de jogador {game.turn}"
            )
        else:
            print("Essa casa já foi escolhida!")
    
    def create_button(self, row, column, game):
        font = ctk.CTkFont(
            family="Segoe UI Variable Display",
            size=30,
            weight="bold"
        )
        button = ctk.CTkButton(
            self.frame,
            text="",
            font=font,
            text_color="#060606",
            width=70,
            height=70,
            border_width=3,
            border_color="#060606",
            fg_color="white",
            hover_color="#ECECEC",
            command=lambda:self.button_click(button=button,
                                        row = row,
                                        column = column,
                                        game = game
                                        )
        )
        return button


    def create_button_array(self, number, game):
        for row in range(number):
            for column in range(number):
                button = self.create_button(row, column, game)
                button.grid(row=row, column=column)
                self.buttons[row][column] = button