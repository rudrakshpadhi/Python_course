import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
game_is_on = True
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager(screen,player)
screen.listen()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.moveUp,'Up') 
    if(player.reachedFinish()):
        cars.increaseSpeed()
        player.return_pos()
        scoreboard.updateLevel()
screen.exitonclick()