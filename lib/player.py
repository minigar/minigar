from lib.rectangle import Rectanle

class Player(Rectanle): 
    def __init__(self, canvas, x, y, width, height, color, keyUp, keyDown):
        
        Rectanle.__init__(self, canvas, x, y, width, height, color)


        self.speed = 50

        if keyUp:
            self.canvas.bind(keyUp, lambda event: self.move(0, -self.speed))
        
        if keyDown:
            self.canvas.bind(keyDown, lambda event: self.move(0, self.speed))

        self.score = 0
