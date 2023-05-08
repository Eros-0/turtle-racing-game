from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()

screen.setup(500, 400)

user_bet = screen.textinput("Make a bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "brown", "green", "blue", "purple"]
y_coordinates = [-60, -30, -0, 30, 60, 90]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # x and y coordinate
    new_turtle.goto(-230, y_coordinates[turtle_index])
    new_turtle.pendown()
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! the {winner} turtle is the winner")
            else:
                print(f"You lost! the {winner} turtle is the winner")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()