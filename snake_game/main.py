from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
scoreBoard = ScoreBoard()
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on = True
while(game_on):
    screen.update()
    time.sleep(0.1)
    snake.movement() 
    if(snake.head.distance(food)<15):
        food.refresh()    
        scoreBoard.updateScore()
        snake.extend()
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 or snake.self_collision()):
        game_on = False 
        scoreBoard.GameOver()   

screen.exitonclick()