import snake_game.config as Config_Map
import snake_game.utils as Utils_Game

fruits_eats = 0
snake_data = (1,1, "d")

def fruits_eat():
    global fruits_eats
    fruts_eats =+ 1

def modify_snake(x,y, direction):
    global snake_data
    snake_data = (x,y, direction)

map_game = Utils_Game.create_map()
def Start_Game():
    pass

