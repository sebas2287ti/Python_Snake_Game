from snake_game.state import dict_direction as direction_snake, map_size, map_game, execute_movent_snake, change_data_snake_temporaly, change_eat_fruits, snake_data, snake_data_temporaly

def check_run_snake_collision():
    snake_y, snake_x, snake_direction = snake_data_temporaly

    map_size_n, map_size_m = map_size

    if snake_y >= 0 and snake_y < map_size_n and snake_x >= 0 and snake_x < map_size_m:
        if map_game[snake_y][snake_x] == 0:
            execute_movent_snake()
            return False
        elif map_game[snake_y][snake_x] == "m":
            execute_movent_snake()
            change_eat_fruits()
            return False
        else:
            return True
    return True


def next_movent_snake():
    snake_y, snake_x, snake_direction_old = snake_data
    new_snake_data = []

    try:
        new_direction = obtener_tecla().lower()
        if new_direction in direction_snake:
            pass
        else:
            raise ValueError("Movimiento no valido")
    except:
        snake_direction_x, snake_direction_y = direction_snake[snake_direction_old] 
        new_snake_data[:] = snake_y + snake_direction_y, snake_x + snake_direction_x, snake_direction_old
    else:
        snake_direction_x, snake_direction_y = direction_snake[new_direction]
        new_snake_data[:] = snake_y + snake_direction_y, snake_x + snake_direction_x, new_direction
    finally:
        change_data_snake_temporaly(new_snake_data)

def obtener_tecla():
    return input("siguiente movimiento: ")

