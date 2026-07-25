from snake_game.utils import dict_direction as direction_snake
from snake_game.config import map_size
from snake_game.game import map_game, fruits_eats, snake_data

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

def movent_snake():
    global snake_data
    y, x, direction = snake_data 
    movent_y, movent_x = direction_snake[direction]

    try:
        tecla = obtener_tecla().lower()
        if tecla in direction_snake:
            pass
        else:
            raise ValueError("Movimiento no valido")
    except: 
        new_y, new_x = y + movent_y, x + movent_x
        snake_data = (new_y,new_x,direction)
    else:
        movent_y, movent_x = direction_snake[tecla]
        new_y, new_x = y + movent_y, x + movent_x
        snake_data = (new_y, new_x, tecla)
    print(snake_data)
    return snake_data 
        

def obtener_tecla():
    return input("movimiento: ")


movent_snake()