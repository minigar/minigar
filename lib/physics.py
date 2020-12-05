import math

REFLECT_RIGHT = 90
REFLECT_LEFT = -90
REFLECT_TOP = -180
REFLECT_BOTTOM = 180

#функция отскока мяча
def reflect_ball(ball, reflect_direction):
    ball.angle = math.pi + 2 * -reflect_direction - ball.angle
    ball.speed_x = math.cos(math.radians(ball.angle)) * ball.speed
    ball.speed_y = math.sin(math.radians(ball.angle)) * ball.speed


# проверка пересикания мяча и ракетки
def is_intersected(ball, paddle):
    if ball.pos_x <= paddle.pos_x + paddle.width and \
        ball.pos_x >= paddle.pos_x - paddle.width and \
        ball.pos_y <= paddle.pos_y + paddle.height and \
        ball.pos_y >= paddle.pos_y - paddle.height:
        return True
    else:
        return False


def reflect_if_intersected(ball, paddle, direction):
    if is_intersected(ball, paddle):
        reflect_ball(ball, direction)
