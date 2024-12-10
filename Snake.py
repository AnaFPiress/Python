import tkinter
import random
from time import sleep


rows = 25
columns = 25
cell_size = 25
TILE_SIZE = 10
window_width = rows * cell_size
window_height = columns * cell_size

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
      



# Game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

# Canvas
canvas = tkinter.Canvas(window, bg = "black", width = window_width, height = window_height, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update

#Center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#Initialize the game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)   
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
velocityX = 0
velocityY = 0

def change_direction(event):
    global velocityX, velocityY

    if event.keysym == "Up":
        velocityX = 0
        velocityY = -1
    elif event.keysym == "Down":
        velocityX = 0
        velocityY = 1
    elif event.keysym == "Left":
        velocityX = -1
        velocityY = 0
    elif event.keysym == "Right":
        velocityX = 1
        velocityY = 0

    

def move_snake():
    global snake
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

   

def draw():
    global snake
    move_snake()

    #Draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green")
    window.after(100, draw)

    #Draw the food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "red")
    window.after(100, draw) 

draw()

window.bind("<KeyPress>", change_direction)
window.mainloop()