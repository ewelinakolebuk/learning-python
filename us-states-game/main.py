import  turtle
from turtle import Turtle

import  pandas
data=pandas.read_csv("50_states.csv")
data_state_name = data.state
print(data_state_name)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states=[]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Gess the State {len(guessed_states)}/50 ",
                                    prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missing_states = [state for state in data_state_name if state not in guessed_states]
        # missing_states=[]   #powyzsza linijka zastępuje te cztery
        # for state in data_state_name:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # # new_data = pandas.DataFrame(missing_states)
        # # new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break


    for state in data_state_name:
        if state == answer_state:
            guessed_states.append(answer_state)
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            state_data = data[data.state==answer_state]
            turtle.goto(state_data.x.item(),state_data.y.item())
            turtle.write(answer_state)
