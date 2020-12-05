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
    reflect_if_intersected(ball, player1, REFLECT_HORISONTALLY)
    reflect_if_intersected(ball, player2, REFLECT_HORISONTALLY)
    reflect_if_intersected(ball, wallTop, REFLECT_VERTICALLY)
    reflect_if_intersected(ball, wallBottom, REFLECT_VERTICALLY)

    if is_intersected(ball, wallLeft):
        player2.score += 1
        canvas.itemconfigure(p_2_text, text=str(player2.score))
        ball.set_position(WIDTH / 2, HEIGHT / 2)
        ball.stop()

    if is_intersected(ball, wallRight):
        player1.score += 1
        canvas.itemconfigure(p_1_text, text=str(player1.score))
        ball.set_position(WIDTH / 2, HEIGHT / 2)
        ball.stop()


    ball.update()
    window.after(30, update)


window, canvas = initialize()

player1 = Player(canvas,
                    10,
                    HEIGHT / 2,
                    PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                    "purple",
                    "<w>",
                    "<s>")

player2 = Player(canvas, 
                    WIDTH + PADDLE_WIDTH - 12,
                    HEIGHT / 2,
                    PADDLE_WIDTH,
                    PADDLE_HEIGHT,
                    "purple",
                    "<Up>",
                    "<Down>")

wallTop = Rectanle(canvas,
                    WIDTH / 2,
                    5,
                    WIDTH,
                    5,
                    "orange")

wallBottom = Rectanle(canvas,
                    WIDTH / 2,
                    HEIGHT - 3,
                    WIDTH,
                    5,
                    "orange")

wallRight = Rectanle(canvas,
                    3,
                    800,
                    WALL_WIGTH,
                    WALL_HEIGHT,
                    "white")

wallLeft = Rectanle(canvas,
                    800,
                    800,
                    WALL_WIGTH,
                    WALL_HEIGHT,
                    "white")

p_1_text = canvas.create_text(
                              WIDTH-WIDTH / 6,
                                PADDLE_HEIGHT / 1,
                                text="0",
                                font="Arial 20",
                                fill="white")

p_2_text = canvas.create_text(WIDTH/6,
                                PADDLE_HEIGHT / 1,
                                text="0",
                                font="Arial 20",
                                fill="white")



ball = Ball(canvas,
            WIDTH / 2,
            HEIGHT / 2,
            10,
            "yellow")

update()

window.mainloop()
