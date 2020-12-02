from tkinter import Canvas


class score:
    def __init__(self, canvas, x, y, width, height, color):
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.paddle = canvas.create_text(
            x - width,
            y - height,
            x + width,
            y + height,
            fill=color)
        

