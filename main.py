# Day 20-21 Project Snake Game

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

print('Welcome to the Snake Game!')
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake_1 = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake_1.up, "Up")
screen.onkey(snake_1.down, "Down")
screen.onkey(snake_1.left, "Left")
screen.onkey(snake_1.right, "Right")

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake_1.move()

    # Detect collision with food
    if snake_1.head.distance(food) < 15:
        food.refresh()
        snake_1.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake_1.head.xcor() > 280 or snake_1.head.xcor() < -280 or snake_1.head.ycor() > 280 or snake_1.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake_1.segments[1:]:
        if snake_1.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
