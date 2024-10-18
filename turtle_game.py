from turtle import Turtle, Screen
import random
import time

# Setup the screen with increased width
screen = Screen()
screen.bgcolor("#333333")
screen.setup(width=800, height=500)  # Increased width to 800


# Countdown function
def countdown():
    countdown_turtle = Turtle()
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.color("white")
    countdown_turtle.goto(0, 0)  # Center the countdown
    for i in range(3, 0, -1):
        countdown_turtle.clear()
        countdown_turtle.write(i, align="center", font=("Arial", 48, "bold"))  # Display countdown number
        time.sleep(1)
    countdown_turtle.clear()
    countdown_turtle.write("Go!", align="center", font=("Arial", 48, "bold"))
    time.sleep(0.5)
    countdown_turtle.clear()


# Initialize race
is_race_on = False
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

# Create turtles
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-350, y_position[turtle_index])  # Start further left to accommodate wider track
    all_turtles.append(new_turtle)

# Start race if user has placed a bet
if user_bet:
    is_race_on = True
    countdown()  # Start countdown before the race

# Create turtles for displaying results
winner_turtle = Turtle()
winner_turtle.hideturtle()
winner_turtle.penup()
winner_turtle.goto(0, 0)  # Center the winner message

loser_turtle = Turtle()
loser_turtle.hideturtle()
loser_turtle.penup()
loser_turtle.goto(0, -70)  # Adjust the position lower for the loser message

# Start the race
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 350:  # Increased finish line position to match track width
            is_race_on = False
            winning_color = turtle.pencolor()
            turtle.shapesize(stretch_wid=2, stretch_len=2)  # Highlight winning turtle

            # Clear previous messages
            winner_turtle.clear()
            loser_turtle.clear()

            # Display winning message
            winner_turtle.color(winning_color)
            winner_turtle.write(f"{winning_color.capitalize()} Wins! 🎉", align="center", font=("Arial", 36, "bold"))

            # Display losing message
            loser_turtle.color("white")
            loser_turtle.write(
                f"You've {'won' if winning_color == user_bet else 'lost'}! The {winning_color} turtle is the winner!",
                align="center", font=("Arial", 24, "normal"))

            break  # Stop the race immediately after the first winner is found

        random_distance = random.randint(0, 10)
        turtle.pendown()
        turtle.forward(random_distance)

# Exit on click
screen.exitonclick()
