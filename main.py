import turtle as t
import time

import scoreboard
import snake

import food
import scoreboard as s

screen=t.Screen()
snake_game=snake.Snake()
screen.listen()
screen.onkey(snake_game.up,"Up")
screen.onkey(snake_game.down,"Down")
screen.onkey(snake_game.right,"Right")
screen.onkey(snake_game.left,"Left")
food_of_turtle=food.Food()


screen.bgcolor("black")
screen.title("My snake game")
screen.setup(width=600,height=600)
screen.tracer(0)
s_b=s.Score_Board()



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_game.move_snake()
    if snake_game.timmies[0].distance(food_of_turtle)<15:
        food_of_turtle.create_food()
        snake_game.extend_snake()

        s_b.refresh_scoreboard()

    if snake_game.timmies[0].xcor() > 295 or snake_game.timmies[0].ycor() > 295 or snake_game.timmies[0].xcor() < -295 or snake_game.timmies[
        0].ycor() < -295:
        game_is_on=False
        s_b.refresh_highscore()
        s_b.game_over()


    for item in snake_game.timmies[1:]:
        if snake_game.timmies[0].distance(item)<10:
            s_b.game_over()
            s_b.refresh_highscore()
            game_is_on=False










screen.exitonclick()
