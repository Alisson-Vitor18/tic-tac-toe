import customtkinter as ctk

def center_window(window, width, height):
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

def create_text(window, message, size):
    font = ctk.CTkFont(
        family="Segoe UI Variable Display",
        size=size,
        weight="bold"
    )

    text = ctk.CTkLabel(
        window, 
        text=message, 
        font=font
    )

    return text

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

    window.mainloop()

tic_tac_toe_interface()