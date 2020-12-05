import math
from tkinter import Canvas

#создаем класс для мяча
class Ball:
    def __init__(self, canvas, x, y, r, color):
        self.pos_x = x
        self.pos_y = y
        self.radius = r
        self.speed = 10
        self.canvas = canvas

        self.ball = canvas.create_oval(
            x - self.radius,
            y - self.radius,
            x + self.radius,
            y + self.radius,
            fill = color
        )

        self.launch()
        self.canvas.bind("<KeyRelease>", lambda event: self.launch() if self.speed_x == 0 and self.speed_y == 0 else False)

    def update(self):

        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        self.canvas.coords(self.ball, 
            self.pos_x - self.radius,
            self.pos_y - self.radius,
            self.pos_x + self.radius,
            self.pos_y + self.radius,
        )

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

        self.canvas.coords(self.ball, 
                            self.pos_x - self.radius,
                            self.pos_y - self.radius,
                            self.pos_x + self.radius,
                            self.pos_y + self.radius)

    def launch(self):
        self.angle = -40
        self.speed_x = math.cos(math.radians(self.angle)) * self.speed
        self.speed_y = math.sin(math.radians(self.angle)) * self.speed

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0