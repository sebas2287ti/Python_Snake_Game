from snake_game.utils import dict_direction as direction_snake
from snake_game.config import map_size
from snake_game.game import map_game, fruits_eats

def check_run_snake_collision(y_snake, x_snake, movent):
    y_movent, x_movent = direction_snake[movent]
    y_next, x_next = y_snake + y_movent, x_snake + x_movent
    map_columnas,map_filas = map_size

    if y_next >= 0 and y_next < map_filas and x_next >= 0 and x_next < map_columnas:
        if  map_game[y_next][x_next] == 0:
            return False
        elif map_game[y_next][x_next] == "f":
            fruits_eats()
            return False
        else:
            return True
    else:
        return True
