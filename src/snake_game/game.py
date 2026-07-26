from snake_game.config import modify_size_map
from snake_game.utils import create_map, print_map
from snake_game.snake import next_movent_snake, check_run_snake_collision

def Start_Game():
    modify_size_map()
    create_map()

    while True:
        print_map() 
        next_movent_snake()
        if check_run_snake_collision():
            input("Colision")
        else:
            pass