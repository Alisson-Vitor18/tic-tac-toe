import customtkinter as ctk
import game as game_logic
import pygame
from tic_tac_toe import TicTacToe
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

def center_window(
        window, 
        width, 
        height
    ):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    scale = window._get_window_scaling()

    x = int(((screen_width - width) // 2) * scale)
    y = int(((screen_height - height) // 2) * scale)

    return f"{width}x{height}+{x}+{y}"

def create_window():
    window = ctk.CTk()

    window.geometry(
        center_window(window, 500, 600)
    )

    window.resizable(False, False)

    return window

def create_text(
        window, 
        message, 
        size
    ):
    font = ctk.CTkFont(
        family="Segoe UI Variable Display",
        size=size,
        weight="bold"
    )

    text = ctk.CTkLabel(
        window, 
        text=message, 
        font=font,
    )

    return text

def restart_game(
        button,
        game, 
        turn_message
    ):

    click_sound.play()
    init_sound.play()

    button.configure(
        state="disabled",
        fg_color="#6A6868",
        hover_color="#6A6868"
    )
    for row in range(3):
        for column in range(3):
            game.board[row][column] = ""
        
            game.buttons[row][column].configure(
                text="",
                fg_color="white",
                hover_color="#ECECEC"
            )
        
    game.turn = "X"
    game.end_game = False
        
    turn_message.configure(text="Vez de jogador X")
    print("Jogo reiniciado!")

def restart_button(
        frame,
        game,
        turn_message
    ):
    font = ctk.CTkFont(
        family="Segoe UI Variable Display", 
        size=28,
        weight="bold"
    )

    button = ctk.CTkButton(
        frame,
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
        command=lambda:restart_game(
            button=button,
            game=game,
            turn_message=turn_message
        )
    )
    button.pack()

    return button

def button_click(
        button,
        row, 
        column,
        turn_message,
        game,
        restart
    ):
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
            turn_message.configure(text=f"Jogador {result} venceu!")
            for row, column in winning_cells:
                game.buttons[row][column].configure(
                    fg_color="#B0CEB1",
                    hover_color="#C6E0C7"
                )
            game.end_game = True
            restart.configure(
                state="normal",
                fg_color="#B0CEB1",
                hover_color="#C6E0C7"
            )
            return
    
        if game_logic.full_board(game.board):
            print("Fim de jogo. Empate!")
            turn_message.configure(text=f"Empate!")
            game.end_game = True
            restart.configure(
                state="normal",
                fg_color="#B0CEB1",
                hover_color="#C6E0C7"
            )
            return
        
        game.swap_turns()
        turn_message.configure(
            text=f"Vez de jogador {game.turn}"
        )

    else:
        print("Essa casa já foi escolhida!")

def create_button(frame,  
                  row, 
                  column, 
                  turn_message,
                  game,
                  restart
                ):
    font = ctk.CTkFont(
        family="Segoe UI Variable Display",
        size=30,
        weight="bold"
    )

    button = ctk.CTkButton(
        frame,
        text="",
        font=font,
        text_color="#060606",
        width=70,
        height=70,
        border_width=3,
        border_color="#060606",
        fg_color="white",
        hover_color="#ECECEC",
        command=lambda:button_click(button, 
                                    row = row,
                                    column = column,
                                    turn_message = turn_message,
                                    game = game,
                                    restart=restart
                                )
    )

    return button

def create_button_array(frame,
                        number, 
                        game,
                        turn_message,
                        restart
                    ):
    for i in range(number):
        for j in range(number):
            button = create_button(frame, 
                                   i, 
                                   j, 
                                   turn_message,
                                   game,
                                   restart
                                )
            button.grid(row=i, column=j)
            game.buttons[i][j] = button

def tic_tac_toe_interface():
    window = create_window()
    window.title("Jogo da Velha")

    title_game = create_text(window, "Jogo da Velha", 40)
    title_game.pack(pady=30)

    turn_message = create_text(window, "Vez de jogador X", 28)
    turn_message.pack()

    frame = ctk.CTkFrame(
        window
    )
    frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    game = TicTacToe()
    restart_frame = ctk.CTkFrame(window)
    
    restart_frame.place(
        relx=0.5,
        rely=0.75,
        anchor="center"
    )
    
    restart = restart_button(
        restart_frame,
        game,
        turn_message
    )

    create_button_array(frame, 
                        3, 
                        game, 
                        turn_message, 
                        restart
                    )

    window.mainloop()

tic_tac_toe_interface()