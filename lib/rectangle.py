class Rectangle:
    def __init__(self, canvas, x, y, width, height, color,):
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.canvas = canvas
       

        self.paddle = self.canvas.create_rectangle(
            x - width,
            y - height,
            x + width,
            y + height,
            fill=color)

        

        
    def move(self, x, y):
        self.pos_x += x
        self.pos_y += y

        self.canvas.coords(self.rectangle, 
            self.pos_x - self.width,
            self.pos_y - self.height,
            self.pos_x + self.width,
            self.pos_y + self.height)
        