import math

#функция отскока мяча
def reflect_ball(ball, paddle):
    ball.angle = math.pi + 2 * -90 - ball.angle
    
    # ball.angle = ball.angle - 180
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


def reflect_if_intersected(ball, paddle):
    if is_intersected(ball, paddle):
        reflect_ball(ball, paddle)

