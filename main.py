from lib.rectangle import Rectangle
from tkinter import *

from settings import *
from lib.score import*
from lib.paddle import Paddle
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
    reflect_if_intersected(ball, paddle1, REFLECT_LEFT)
    reflect_if_intersected(ball, paddle2, REFLECT_RIGHT)
    reflect_if_intersected(ball, paddle3, REFLECT_BOTTOM)
    reflect_if_intersected(ball, paddle4, REFLECT_TOP)

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
paddle3 = Rectangle(canvas,
                    800,
                    5,
                    RECTANGLE_WIDTH,
                    RECTANGLE_HEIGHT,
                    "yellow",
                    )

paddle4 = Rectangle(canvas,
                    800,
                    HEIGHT + PADDLE_HEIGHT - 52,
                    RECTANGLE_WIDTH,
                    RECTANGLE_HEIGHT,
                    "yellow",
                    )

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

def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        canvas.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        canvas.itemconfig(p_2_text, text=PLAYER_2_SCORE)
 
def spawn_ball():
    global BALL_X_SPEED
    # Выставляем мяч по центру
    canvas.coords(ball, WIDTH/2-BALL_RADIUS/2,
             HEIGHT/2-BALL_RADIUS/2,
             WIDTH/2+BALL_RADIUS/2,
             HEIGHT/2+BALL_RADIUS/2)
    # Задаем мячу направление в сторону проигравшего игрока,
    # но снижаем скорость до изначальной
    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)

    


update()

window.mainloop()
