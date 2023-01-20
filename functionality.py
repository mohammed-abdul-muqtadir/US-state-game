from turtle import Turtle
import pandas as pd
states_data = pd.read_csv('50_states.csv')


class Functionality:
    def __init__(self):
        self.count = 0
        self.states_guessed = []
        self.learn = []

    def checker(self, answer_state):
        for i in states_data['state']:
            if i == answer_state:
                self.writter(answer_state)
                self.count += 1
                self.states_guessed.append(answer_state)
        if answer_state == "Exit":
            self.states_to_learn()


    def writter(self, ans):
        state = Turtle()
        state.penup()
        state.color("black")
        state.hideturtle()
        xx = states_data[states_data['state'] == ans]
        y = (int(xx['y']))
        x = (int(xx['x']))
        state.goto(x=x, y=y)
        state.write(f"{ans}")

    def states_to_learn(self):
        for state in states_data['state']:
            if state not in self.states_guessed:
                self.learn.append(state)
        data = pd.DataFrame(self.learn)
        data.to_csv("states_to_learn.csv")


    def youWon(self):
        t = Turtle()
        t.hideturtle()
        t.write("You won congratulation", align="center", font=("Arial", 50, "normal"))
