from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []

game_is_on = True
while game_is_on:
    car_manager = CarManager()
    cars.append(car_manager)
    for car in cars:
        car.move_car()
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on = False
            break

    time.sleep(0.25)
    screen.update()
    screen.onkey(player.move_turtle, 'Up')
    screen.listen()
    
    if player.ycor() >= 280:
        player.finish_line()
        scoreboard.point()

    if car_manager.xcor() <= 0:
        print(car_manager.xcor())
        # car_manager.destroy_car()
    


screen.exitonclick()