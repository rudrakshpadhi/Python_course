from turtle import Turtle,Screen
import random
import heroes as h
timmy = Turtle()
timmy.shape("classic")
timmy.color("blue")
# for i in range(0,4):
#     timmy.forward(100)
#     timmy.left(90)
# for i in range(0,50):
#     if(i%2==0):
#         timmy.color("white")
#         timmy.forward(5)
#         timmy.color("black")
#         timmy.forward(5)
# for i in range(3,11):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     timmy.color(r,g,b)
#     for j in range(0,i):
#         timmy.left(360/i)
#         timmy.forward(100)
timmy.speed(10)
timmy.width(10)
angles = [0,90,180,270]
colors = ["blue","red","green","yellow"]
for i in range(100):
    timmy.right(random.choice(angles))
    timmy.forward(50)
    timmy.color(random.choice(colors))
      
screen = Screen()
screen.exitonclick()
