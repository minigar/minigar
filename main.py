from tkinter import *

from settings import *
from lib.score import*
from lib.player import Player
from lib.rectangle import Rectanle
from lib.ball import Ball
from lib.physics import *

# Сделать две ракетки которіми нельзя двигать, расположить в крайних положениях верх и низ, и добавить отражение мячика

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
    reflect_if_intersected(ball, paddle1, REFLECT_HORISONTALLY)
    reflect_if_intersected(ball, paddle2, REFLECT_HORISONTALLY)
    reflect_if_intersected(ball, paddle3, REFLECT_VERTICALLY)
    reflect_if_intersected(ball, paddle4, REFLECT_VERTICALLY)

    ball.update()
    window.after(30, update)


window, canvas = initialize()

paddle1 = Paddle(canvas,
                    10,
                    HEIGHT / 2,
                    PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                    "purple",
                    "<w>",
                    "<s>")

paddle2 = Paddle(canvas, 
                    WIDTH + PADDLE_WIDTH - 10,
                    HEIGHT / 2,
                    PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                    "purple",
                    "<Up>",
                    "<Down>")
paddle3 = Paddle(canvas,
                    800,
                    5,
                    RECTANGLE_WIDTH,
                    RECTANGLE_HEIGHT,
                    "orange",
                    False,
                    False)

paddle4 = Paddle(canvas,
                    800,
                    HEIGHT + PADDLE_HEIGHT - 52,
                    RECTANGLE_WIDTH,
                    RECTANGLE_HEIGHT,
                    "orange",
                    False,
                    False)

p_1_text = canvas.create_text(
                              WIDTH-WIDTH/6,
                                PADDLE_HEIGHT/1,
                                text=PLAYER_1_SCORE,
                                font="Arial 20",
                                fill="white")

p_2_text = canvas.create_text(WIDTH/6,
                                PADDLE_HEIGHT/1,
                                text=PLAYER_2_SCORE,
                                font="Arial 20",
                                fill="white")



ball = Ball(canvas, WIDTH / 2, HEIGHT / 2, 10, "yellow")

update()

window.mainloop()
