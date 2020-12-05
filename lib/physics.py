import math

REFLECT_HORISONTALLY = 90
REFLECT_VERTICALLY = 180

#функция отскока мяча
def reflect_ball(ball, reflect_direction):
    ball.angle = math.pi + 2 * reflect_direction - ball.angle
    ball.speed_x = math.cos(math.radians(ball.angle)) * ball.speed
    ball.speed_y = math.sin(math.radians(ball.angle)) * ball.speed


# проверка пересикания мяча и ракетки
def is_intersected(ball, rect):
    if ball.pos_x <= rect.pos_x + rect.width and \
        ball.pos_x >= rect.pos_x - rect.width and \
        ball.pos_y <= rect.pos_y + rect.height and \
        ball.pos_y >= rect.pos_y - rect.height:
        return True
    else:
        return False


def reflect_if_intersected(ball, paddle, direction):
    if is_intersected(ball, paddle):
        reflect_ball(ball, direction)
