import tkinter
import random  

# Constants
rows = 25
columns = 25
cell_size = 25

window_width =rows * cell_size
window_height = columns * cell_size

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

# canvas
canvas = tkinter.Canvas(window, bg="black", width=window_width, height=window_height, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

# center the window
window_width = window.winfo_width()
window_height = window.winfo_height()   
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#Initialize the game
snake = Tile(5*cell_size, 5*cell_size)
Food = Tile(10*cell_size, 10*cell_size)
snake_body = [] # multiple tiles 
velocityX = 0
velocityY = 0
game_over = False
score = 0

def change_direction(event):
    global velocityX, velocityY, game_over
    if (game_over):
        return
    
    if (event.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (event.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (event.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (event.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0
        
def move_snake():
    global snake, Food, snake_body, game_over, score
    
    # Check for collision and stop the movement
    if (game_over):
        return
    
    # Check for collision with the walls
    if (snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height):
        game_over = True
        return
    
    # check for collision with itself
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return
    
    
    #Colision for the food and snake
    if (snake.x == Food.x and snake.y == Food.y):
        snake_body.append(Tile(Food.x, Food.y))
        Food.x = random.randint(0, columns-1) * cell_size
        Food.y = random.randint(0, rows-1) * cell_size
        score += 1
        
    #Update the snake body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if(i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
        
        
    #Move the snake
    snake.x += velocityX * cell_size
    snake.y += velocityY * cell_size
 

def draw_snake():
    global snake, Food, snake_body, game_over, score
    move_snake()
    
    #chek to clear the previous frame
    canvas.delete("all")
    
    #draw the food
    canvas.create_rectangle(Food.x, Food.y, Food.x + cell_size, Food.y + cell_size, fill="red")
    
    
    # draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + cell_size, snake.y + cell_size, fill="limegreen")   
 
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + cell_size, tile.y + cell_size, fill="limegreen")
    
    if (game_over):
        canvas.create_text(window_width/2, window_height/2, text=f"Game Over! Score: {score}", fill="white", font=("Arial", 24))
        return
    else:
        canvas.create_text(30, 20, font=("Arial", 16), text=f"Score: {score}", fill="white")
    window.after(100, draw_snake)

draw_snake()

window.bind("<KeyRelease>", change_direction) 
window.mainloop()   