""" calls score object from scoreboard file
 snake object from the snake file
 food object from the food file
 """
from turtle import Screen
import time
from scoreboard import Score
from snake import Snake
from food import Food

main_screen = Screen()
main_screen.setup(width = 1000, height = 800)
main_screen.bgcolor("black")
main_screen.title("Snake Game")
main_screen.tracer(0)

game_is_on = True
main_snake = Snake()
main_snake_head = main_snake.body_list[0]
main_food = Food()
main_score = Score()
main_screen.update()
main_screen.listen()
while game_is_on:
    main_snake.move()
    main_screen.onkey(key = "Up",fun = main_snake.up)
    main_screen.onkey(key = "Down",fun = main_snake.down)
    main_screen.onkey(key = "Left",fun = main_snake.turn_left)
    main_screen.onkey(key = "Right",fun = main_snake.turn_right)
    # If the food on the screen is closer than 15 to the snake head, creates new food,
    # then updates the score +1 and adds a new body to the snake.
    if main_food.distance(main_snake_head)<=15:
        main_food.new_food()
        main_score.update()
    # A wall collision check if the head of the snake passes any of the
    # boundaries then, call reset and update the high score if the score is higher than a high score
    # message and restart the loop.
    if main_snake_head.xcor() > 460 or main_snake_head.xcor() < -480\
        or main_snake_head.ycor() > 340 or main_snake_head.ycor() < -340:
        main_score.gameover()
        game_is_on = False

    # A tail collision check if the head of the snake is close to
    # bany part of the snake body apart from itself, calls reset and update high score if the score 
    # is higher than the high score message and restart the loop.
    if main_snake.tail_collision():
        main_score.gameover()
        game_is_on = False
    main_screen.update()
    time.sleep(0.1)


main_screen.exitonclick()
