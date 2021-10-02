import turtle
import pandas


BACKGROUND = "blank_states_img.gif"

screen = turtle.Screen()
#gives game a title
screen.title("United States Game")

#sets the background 
screen.bgpic(BACKGROUND)

#Alternative way of setting the background
"""screen.addshape(BACKGROUND)
turtle.shape(BACKGROUND)"""



data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

correct_guesses = []
state_count = len(correct_guesses)

#1 - Convert guess to Title Case
#2 - Check if guess is among the 50 States
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Correct States", prompt="What is a state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in list_of_states if state not in correct_guesses]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("States to Learn.csv")
        break
    if answer_state in list_of_states:
        correct_guesses.append(answer_state)
        ganke = turtle.Turtle()
        ganke.hideturtle()
        ganke.penup()
        state_data = data[data.state == answer_state]
        ganke.goto(int(state_data.x), int(state_data.y))
        ganke.write(answer_state)
        #alternative - ganke.write(data.state.item()) - not necessary because we already checked the answer 
        
        state_count += 1
    #print(correct_guesses)
#3 - Write correct guesses on map
#4 - Write a loop to allow user to keep guessing
#5 - Record correct guesses in a list
#6 - Keep track of score
#7 ** Not really a bonus, but update screen.title dynamically with the correct number of guesses
#8 ** Bonus - add a "give up" button
