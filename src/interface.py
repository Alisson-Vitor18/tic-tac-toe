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
        font=font,
    )

    return text

def restart_game(
        button,
        board, 
        buttons, 
        state, 
        end_game, 
        turn_message
    ):
    button.configure(
        state="disabled",
        fg_color="#6A6868",
        hover_color="#6A6868"
    )
    for row in range(3):
        for column in range(3):
            board[row][column] = ""
        
            buttons[row][column].configure(
                text="",
                fg_color="white",
                hover_color="#ECECEC"
            )
        
    state["turn"] = "X"
    end_game["end"] = False
        
    turn_message.configure(text="Vez de jogador X")

def restart_button(
        frame,
        board,
        buttons,
        state,
        end_game,
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
            board=board,
            buttons=buttons,  
            state=state,
            end_game=end_game,
            turn_message=turn_message
        )
    )
    button.pack()

    return button

def button_click(
        button,
        state,
        row, 
        column,
        board,
        turn_message,
        buttons,
        end_game,
        restart
    ):
    if end_game["end"]:
        return

    if game.valid_move(board, row, column):
        button.configure(
            fg_color= "#E4E4E4",
            text = state["turn"]
            )

        board[row][column] = state["turn"]

        result, winning_cells = game.check_win(board)

        if result is not None:
            print(f"Fim de jogo. jogador {result} venceu!")
            turn_message.configure(text=f"Jogador {result} venceu!")
            for row, column in winning_cells:
                buttons[row][column].configure(
                    fg_color="#B0CEB1",
                    hover_color="#C6E0C7"
                )
            end_game["end"] = True
            restart.configure(
                state="normal",
                fg_color="#B0CEB1",
                hover_color="#C6E0C7"
            )
            return
    
        if game.full_board(board):
            print("Fim de jogo. Empate!")
            turn_message.configure(text=f"Empate!")
            end_game["end"] = True
            restart.configure(
                state="normal",
                fg_color="#B0CEB1",
                hover_color="#C6E0C7"
            )
            return
        
        game.swap_turns(state)
        turn_message.configure(
            text=f"Vez de jogador {state['turn']}"
        )

    else:
        print("Essa casa já foi escolhida!")

def create_button(frame, 
                  state, 
                  row, 
                  column, 
                  board, 
                  turn_message,
                  buttons,
                  end_game,
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
                                    state = state, 
                                    row = row,
                                    column = column,
                                    board = board,
                                    turn_message = turn_message,
                                    buttons = buttons,
                                    end_game = end_game,
                                    restart=restart
                                    )
    )

    return button

def create_button_array(frame,
                        number, 
                        state, 
                        buttons, 
                        board, 
                        turn_message,
                        end_game,
                        restart
                    ):
    for i in range(number):
        for j in range(number):
            button = create_button(frame, 
                                   state, 
                                   i, 
                                   j, 
                                   board,
                                   turn_message,
                                   buttons,
                                   end_game,
                                   restart
                                )
            button.grid(row=i, column=j)
            buttons[i][j] = button

def create_game_state():
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
    end_game = {"end": False}

    return buttons, board, state, end_game

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

    buttons, board , state, end_game = create_game_state()

    restart_frame = ctk.CTkFrame(window)
    
    restart_frame.place(
        relx=0.5,
        rely=0.75,
        anchor="center"
    )
    
    restart = restart_button(
        restart_frame,
        board,
        buttons,
        state,
        end_game,
        turn_message
    )

    create_button_array(frame, 
                        3, 
                        state, 
                        buttons, 
                        board, 
                        turn_message, 
                        end_game,
                        restart
                    )

    window.mainloop()

tic_tac_toe_interface()