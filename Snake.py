import tkinter
import random


rows = 25
columns = 25
cell_size = 25

window_width = rows * cell_size
window_height = columns * cell_size


# Game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

# Canvas
canvas = tkinter.Canvas(window, bg = "black", width = window_width, height = window_height)
canvas.pack()
window


window.mainloop