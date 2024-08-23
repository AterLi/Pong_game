# 1. Create two clases of the wall, one in the left side other right side
# 2. It should move by tapping the keys on the keyboard
# 3. Class of the ball, that should bounce if it hit the gamer wall, also bounce from -y, and y, if it hits x, or -x
# game over, game starts again
# 4. Score clase based on two gamers, if left hit the wall of right one he gains a point, and viceversa
# 5. Class Make delimitation on y axes of intrerupted linse/turtles

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title(titlestring="Welcome to Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Defining paddles
right_pad = Paddle((350, 0))
left_pad = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
# Right commands
screen.onkeypress(right_pad.up, "Up")
screen.onkeypress(right_pad.down, "Down")
# Left commands
screen.onkeypress(left_pad.up, "w")
screen.onkeypress(left_pad.down, "s")

# Updates the screen after removing animation of created objects/turtles by screen.tracer
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # If ball hits upper or lower wall it should bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect colision with r_paddle
    if (ball.distance(right_pad) < 50 and ball.xcor() > 325) or (ball.distance(left_pad) < 50 and ball.xcor() < -325):
        ball.bounce_x()

    # Detect when the ball was missed and restart the game
    # For right side misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.point_for_l()
    # For left side
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.point_for_r()




screen.exitonclick()

