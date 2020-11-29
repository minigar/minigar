import math

#создаем класс для мяча
class Ball:
    def __init__(self, canvas, x, y, r, color):
        self.pos_x = x
        self.pos_y = y
        self.radius = r
        self.ball_speed = 10
        self.canvas = canvas

        self.ball = canvas.create_oval(
            x - self.radius,
            y - self.radius,
            x + self.radius,
            y + self.radius,
            fill = color
        )

        self.angle = -5
        self.speed_x = math.cos(math.radians(self.angle)) * self.ball_speed
        self.speed_y = math.sin(math.radians(self.angle)) * self.ball_speed
        

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        self.canvas.coords(self.ball, 
            self.pos_x - self.radius,
            self.pos_y - self.radius,
            self.pos_x + self.radius,
            self.pos_y + self.radius,
        )

    #функция отскока мяча
    def reflect(self):
        self.angle = math.pi + 2 * -90 - self.angle
        # self.angle = self.angle - 180
        self.speed_x = math.cos(math.radians(self.angle)) * self.ball_speed
        self.speed_y = math.sin(math.radians(self.angle)) * self.ball_speed


    # проверка пересикания мяча и ракетки
    def is_intersected(self, paddle):
        if self.pos_x <= paddle.pos_x + paddle.width and \
            self.pos_x >= paddle.pos_x - paddle.width and \
            self.pos_y <= paddle.pos_y + paddle.height and \
            self.pos_y >= paddle.pos_y - paddle.height:
            return True
        else:
            return False

    def reflect_if_intersected(self, paddle):
        if self.is_intersected(paddle):
            self.reflect()

