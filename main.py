from tkinter import *

from lib.paddle import Paddle
from lib.ball import Ball
from settings import *

# устанавливаем окно
def initialize():
    window = Tk()
    window.title("PING PONG")
    window.resizable(width = False, height = False)

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, background=BG)
    canvas.pack()
    canvas.focus_set()
    canvas.bind("<Escape>", lambda event: exit())

    canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")
    
    return window, canvas

def update():
    ball.reflect_if_intersected(paddle1)
    ball.reflect_if_intersected(paddle2)
    ball.update()
    window.after(30, update)


window, canvas = initialize()

paddle1 = Paddle(canvas,
                    10,
                    HEIGHT / 2,
                    PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                    "#ff0000",
                    "<w>",
                    "<s>")

paddle2 = Paddle(canvas, 
                    WIDTH + PADDLE_WIDTH - 10,
                    HEIGHT / 2, PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                    "#00ff00",
                    "<Up>",
                    "<Down>")

ball = Ball(canvas, WIDTH / 2, HEIGHT / 2, 10, "yellow")

update()

window.mainloop()
