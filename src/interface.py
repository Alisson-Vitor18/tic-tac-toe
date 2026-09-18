import customtkinter as ctk
from tic_tac_toe_interface import TicTacToeInterface
from tic_tac_toe import TicTacToe

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
        game, 
        interface
    ):

    #click_sound.play()
    #init_sound.play()

    interface.restart_button.configure(
        state="disabled",
        fg_color="#6A6868",
        hover_color="#6A6868"
    )
    for row in range(3):
        for column in range(3):
            game.board[row][column] = ""
        
            interface.buttons[row][column].configure(
                text="",
                fg_color="white",
                hover_color="#ECECEC"
            )
        
    game.turn = "X"
    game.end_game = False
        
    interface.turn_message.configure(text="Vez de jogador X")
    print("Jogo reiniciado!")

def restart_button(
        game,
        interface
    ):
    font = ctk.CTkFont(
        family="Segoe UI Variable Display", 
        size=28,
        weight="bold"
    )

    button = ctk.CTkButton(
        interface.restart_frame,
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
            game=game,
            interface=interface
        )
    )
    button.pack()

    return button

def tic_tac_toe_interface():
    interface = TicTacToeInterface()
    interface.window.title("Jogo da Velha")

    interface.title_game = create_text(interface.window, "Jogo da Velha", 40)
    interface.title_game.pack(pady=30)

    interface.turn_message = create_text(interface.window, "Vez de jogador X", 28)
    interface.turn_message.pack()

    interface.frame = ctk.CTkFrame(
        interface.window
    )
    interface.frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    game = TicTacToe()
    interface.restart_frame = ctk.CTkFrame(interface.window)
    
    interface.restart_frame.place(
        relx=0.5,
        rely=0.75,
        anchor="center"
    )
    
    interface.restart_button = restart_button(
        game,
        interface
    )

    interface.create_button_array(3, game)

    interface.window.mainloop()

tic_tac_toe_interface()