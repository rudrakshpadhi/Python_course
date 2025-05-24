from turtle import Turtle,Screen
import pandas as pd
STATE_DATA = pd.read_csv("50_states.csv")
states = STATE_DATA.state.tolist()
states = ["Michigan"]
screen = Screen()
screen.title("US States game")
screen.addshape("blank_states_img.gif")
background = Turtle()
background.shape("blank_states_img.gif")

def findCoord(STATE_DATA,input):
    req_state = STATE_DATA[STATE_DATA["state"]==input]
    return (req_state["x"].iloc[0],req_state["y"].iloc[0])


while len(states)>0:
    user_in = (screen.textinput(title="Guess a state",prompt="Enter a valid US state")).strip().title()
    if user_in in states:
        move = Turtle()
        move.hideturtle()
        move.penup()
        move.goto(findCoord(STATE_DATA,user_in))
        move.write(user_in)
        states.remove(user_in)

screen.exitonclick()