import snake_game.config as Config_Map
import snake_game.utils as Utils_Game

fruits_eats = 0
snake_data = [1,1, "d"]

def fruits_eat():
    global fruits_eats
    fruts_eats =+ 1

def modify_snake(x,y, direction):
    global snake_data
    snake_data[:] = x,y, direction

def Start_Game():
    Config_Map.modify_size_map()
    Utils_Game.create_map()

    while True:
        
        Utils_Game.print_map()

