import turtle
import pandas

# Screen Setup
screen = turtle.Screen()
screen.setup(width=750, height=510)
screen.title("U.S. States Game")

# Background Image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Turtle setup
printer = turtle.Turtle()
printer.penup()
printer.hideturtle()


# Function to move turtle and print text
def print_text(x, y, us_state):
    printer.goto(x, y)
    printer.write(f"{us_state}", align="center", font=('Arial', 8, 'normal'))


# Import Data
df = pandas.read_csv("50_states.csv")


# Repeat game until all states are done
score = 0
state_list = df.state.to_list()

while score != 50:
    # User Input
    answer_state = screen.textinput(title=f"Guess the state {score}/50", prompt="Enter state").title()
    # Compare User Input and Data
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        state_list.remove(answer_state)
        row = df[df.state == answer_state]
        print_text(float(row.x), float(row.y), answer_state)
        score += 1
    if score == 50:
        printer.goto(0, 480)
        printer.write("Finished", align="center", font=('Arial', 20, 'normal'))

df2 = pandas.DataFrame(state_list)
df2.to_csv("missing_state.csv")

