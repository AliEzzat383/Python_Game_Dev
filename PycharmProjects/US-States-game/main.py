import turtle
import pandas

FONT = ("Arial", 12, "normal")
ALIGNMENT = "center"


def us_game():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.tolist()
    correct = []
    remaining = state_list
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name ?")
    answer_state = str(answer_state).title()
    while len(correct) < 50:
        if answer_state in state_list:
            states = turtle.Turtle()
            states.penup()
            states.ht()
            ans = data[data.state == answer_state]
            states.goto(int(ans.x), int(ans.y))
            states.write(f"{answer_state}", False, ALIGNMENT, FONT)
            correct.append(answer_state)
            remaining.remove(answer_state)
        elif answer_state == "Off":
            df = pandas.DataFrame(remaining)
            df.to_csv("remaining_states.csv")
            exit()
        else:
            pass
        answer_state = screen.textinput(title=f"{len(correct)}/50 States correct", prompt="What's another state name ?")
        answer_state = str(answer_state).title()
    turtle.exitonclick()



us_game()
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
