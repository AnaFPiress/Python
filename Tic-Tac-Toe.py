import tkinter

def set_title(row, column):
    global current_player

    if (game_over):
        return

    if board[row][column]["text"] !="":
        return

    board[row][column]["text"] = current_player

    if current_player == player1:
        current_player = player2
    else: 
        current_player = player1

    label["text"] = current_player+"s turn"

    winner_condition()

# winner condicion
def winner_condition():
    global turns, game_over
    turns +=1 

    # horizontally
    for row in range(3): 
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winer!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            game_over = True
            return
        
    #Vertically
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            game_over = True
            return
    
    #Diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for  i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_grey)
        game_over = True
        return

    # anti-diagonally
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[2][0]["text"] != ""):
       label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
       board[0][2].config(foreground=color_yellow, background=color_light_grey)
       board[1][1].config(foreground=color_yellow, background=color_light_grey)
       board[2][0].config(foreground=color_yellow, background=color_light_grey)
       game_over = True
       return

    # Tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

def new_game():
    global turns, game_over
    turns = 0
    game_over = False

    label.config(text=current_player+"s turn", foreground="white")

    for  row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_Blue, background=color_grey)

#Game setup
player1 = 'X'
player2 ='O'
current_player = player1
board = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

color_Blue = "#4584b6"
color_yellow = "#ffde57"
color_grey = "#343434"
color_light_grey = "#646464"


#Windw setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

turns = 0
game_over = False

frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=current_player+"s turn", font=("consolas", 20), background = color_grey, foreground= "white")
label.grid(column=0, row=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas", 50, "bold"), 
                                            background=color_grey, foreground=color_Blue, width=4, height=1, 
                                            command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("consolas", 20), background=color_grey, foreground="white", command=new_game) 

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screeen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screeen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))


# format
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()