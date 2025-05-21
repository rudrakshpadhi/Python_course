from turtle import Screen,Turtle
from dashed import Dashed
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.setup(1200,700)
screen.bgcolor("black")
screen.tracer(0)
dash = Dashed()
paddles = []
paddles.append(Paddle(0))
paddles.append(Paddle(1))
def moveLeftPaddleUp():
    paddles[0].paddle_up()
    screen.update()
def moveLeftPaddleDown():
    paddles[0].paddle_down()
    screen.update()
def moveRightPaddleUp():
    paddles[1].paddle_up()
    screen.update()
def moveRightPaddleDown():
    paddles[1].paddle_down() 
    screen.update()   
ball = Ball(paddles,screen)
screen.update()
screen.listen()
screen.onkey(paddles[0].paddle_up,'w')

screen.onkey(paddles[0].paddle_down,'s')

screen.onkey(paddles[1].paddle_up,'Up')

screen.onkey(paddles[1].paddle_down,'Down')

screen.exitonclick()

