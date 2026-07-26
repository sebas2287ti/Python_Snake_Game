map_size = [10, 10]

map_game = []

fruits_eats = 0

snake_data = [1,1,"d"]
snake_data_temporaly = []
snake_data_old = []

snake_form = {
    "w":"△",
    "a":"◁",
    "d":"▷",
    "s":"▽"
}

dict_direction = { 
    "w":(0,-1),
    "a":(-1,0),
    "d":(1,0),
    "s":(0,1)
}


def change_eat_fruits():
    global fruits_eats
    fruts_eats =+ 1

def change_data_snake_temporaly(new_snake_data):
    global snake_data_temporaly
    snake_data_temporaly[:] = new_snake_data

def execute_movent_snake():
    global snake_data_temporaly
    global snake_data
    global snake_data_old

    snake_data_old[:] = snake_data
    snake_data[:] = snake_data_temporaly
    snake_data_temporaly[:] = []

    snake_y_old, snake_x_old, snake_direction_old = snake_data_old
    snake_y, snake_x, snake_direction = snake_data

    map_game[snake_y_old][snake_x_old] = snake_direction
    map_game[snake_y][snake_x] = snake_form[snake_direction]

def change_map_size(n, m):
    global map_size
    map_size[:] = n,m

def change_map_game(new_map):
    global map_game
    map_game[:] = new_map

