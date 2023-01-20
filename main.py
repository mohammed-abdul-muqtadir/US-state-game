import turtle
import pandas as pd
from functionality import Functionality

screen = turtle.Screen()
screen.title("U.S State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_data = pd.read_csv('50_states.csv')
functionality = Functionality()

guessed_states = []
i = 50
while functionality.count <= i:
    answer_state = turtle.textinput(title=f"{functionality.count}/{50} State Correct",
                                    prompt="What the name of the state?").lower()
    answer_state = answer_state[0].upper() + answer_state[1:]
    functionality.checker(answer_state)
    if answer_state == 'Exit':
        i = 100
if functionality.count == 50:
    functionality.youWon()
screen.exitonclick()
