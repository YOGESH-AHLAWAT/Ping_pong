import turtle
import time
import scoreboard
import paddle
import ball

score = scoreboard.Score()
ball = ball.Ball()
screen = turtle.Screen()
screen.bgcolor("Black")
middle = turtle.Turtle('square')
middle.color('white')
middle.shapesize(100, 0.01)
screen.setup(800, 600)
screen.title("Ping Pong Game")
screen.listen()
screen.tracer(0)
r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
screen.onkey(fun=r_paddle.move_up, key='Up')
screen.onkey(fun=r_paddle.move_down, key='Down')
screen.onkey(fun=l_paddle.move_up, key='w')
screen.onkey(fun=l_paddle.move_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        # then bounce
        ball.bounce_y()

    # collision with paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # when ball missed RHS
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_player_score()
    # when ball missed LHS
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_player_score()

screen.exitonclick()
