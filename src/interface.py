import customtkinter as ctk
import game

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

def button_click(
        button,
        state,
        row, 
        column,
        board,
        turn_message
    ):

    if game.valid_move(board, row, column):
        button.configure(fg_color= "#E4E4E4")
        
        if state["turn"] == "X":
            button.configure(text="X")
            board[row][column] = "X"
            state["turn"] = "O"
        else: 
            button.configure(text="O")
            board[row][column] = "O"
            state["turn"] = "X"

        result = game.check_win(board)

        if result is not None:
            print(f"Fim de jogo. jogador {result} venceu!")
            turn_message.configure(text=f"Jogador {result} venceu!")
            return

        if game.full_board(board):
            print("Fim de jogo. Empate!")
            turn_message.configure(text=f"Empate!")
            return
        
        turn_message.configure(text=f"Vez de jogador {state['turn']}")

    else:
        print("Essa casa já foi escolhida!")

def create_button(frame, 
                  state, 
                  row, 
                  column, 
                  board, 
                  turn_message
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
                                    state = state, 
                                    row = row,
                                    column = column,
                                    board = board,
                                    turn_message = turn_message
                                    )
    )

    return button

def create_button_array(frame,
                        number, 
                        state, 
                        buttons, 
                        board, 
                        turn_message 
                    ):
    for i in range(number):
        for j in range(number):
            button = create_button(frame, 
                                   state, 
                                   i, 
                                   j, 
                                   board,
                                   turn_message
                                )
            button.grid(row=i, column=j)
            buttons[i][j] = button

def utility():
    buttons = [
        [None,None, None],
        [None,None, None],
        [None,None, None],
    ]

    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    state = {"turn": "X"}

    return buttons, board, state

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

    buttons, board , state = utility()

    create_button_array(frame, 3, state, buttons, board, turn_message )

    window.mainloop()

tic_tac_toe_interface()