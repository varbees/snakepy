from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#085e43')
screen.title("SnakePy")
# tracer toggle 0-off 1-on use update method to refresh screen
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = scoreboard.score

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

# def tryagain():
#     global game_is_on
#     if screen.onkeypress(snake.space, 'space') == True:
#         game_is_on = True
#     else:
#         pass

while game_is_on:
    screen.update()
    time.sleep(0.14)
    snake.move()

    # Detect Collisions with food
    if snake.snakehead.distance(food) < 15:
        food.refresh()
        snake.extend_snake()      
        scoreboard.increase_score()

    # Wall collision Detection
    if snake.snakehead.xcor() > 290 or snake.snakehead.xcor() < -290 or snake.snakehead.ycor() > 290 or snake.snakehead.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()  
        # tryagain()


    # snake body collision detection
    without_head = snake.segments[1:]
    for segment in without_head:
        if snake.snakehead.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            



screen.exitonclick()
