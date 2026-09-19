import customtkinter as ctk
from tic_tac_toe_interface import TicTacToeInterface

def tic_tac_toe_interface():
    interface = TicTacToeInterface()
    interface.window.title("Jogo da Velha")

    interface.create_title_game()
    interface.create_turn_message_text()

    interface.frame = ctk.CTkFrame(
        interface.window
    )
    interface.frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    interface.restart_frame = ctk.CTkFrame(interface.window)
    
    interface.restart_frame.place(
        relx=0.5,
        rely=0.75,
        anchor="center"
    )
    
    interface.create_restart_button()

    interface.create_button_array(3)

    interface.window.mainloop()

tic_tac_toe_interface()