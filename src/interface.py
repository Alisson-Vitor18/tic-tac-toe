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
    
    interface.restart_button = interface.create_restart_button(game)

    interface.create_button_array(3, game)

    interface.window.mainloop()

tic_tac_toe_interface()