from turtle import Screen
from time import sleep
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

RIGHT_PADDLE_X_POSITION = (350, 0)
LEFT_PADDLE_X_POSITION = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

screen.tracer(0)

r_paddle = Paddle(RIGHT_PADDLE_X_POSITION)

l_paddle = Paddle(LEFT_PADDLE_X_POSITION)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.change_direction_wall()
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -330) or (ball.distance(r_paddle) < 50 and ball.xcor() > 330):
        ball.change_direction_paddle()
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.goal()
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.goal()

screen.exitonclick()
