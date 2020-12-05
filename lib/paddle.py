class Paddle:
    def __init__(self, canvas, x, y, width, height, color, keyUp, keyDown):
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.speed = 50

        self.paddle = self.canvas.create_rectangle(
            x - width,
            y - height,
            x + width,
            y + height,
            fill=color)

        if keyUp:
            self.canvas.bind(keyUp, lambda event: self.move(0, -self.speed))
        
        if keyDown:
            self.canvas.bind(keyDown, lambda event: self.move(0, self.speed))
            
            
        
        
    def move(self, x, y):
        self.pos_x += x
        self.pos_y += y

        self.canvas.coords(self.paddle, 
            self.pos_x - self.width,
            self.pos_y - self.height,
            self.pos_x + self.width,
            self.pos_y + self.height)
    