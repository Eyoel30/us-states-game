from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
screen.title("U.S stat game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 state correct",
                                    prompt="what is another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_state]
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        turtle.hideturtle()
        turtle.penup()
        state_data = data[data.state == answer_state]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(answer_state)

