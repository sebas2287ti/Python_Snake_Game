map_size = [10, 10]

map_game = []

fruits_eats = 0

snake_data = [1,1,"d"]

dict_direction = { 
    "a":(0,-1),
    "w":(-1,0),
    "s":(1,0),
    "d":(0,1)
}


def change_eat_fruits():
    global fruits_eats
    fruts_eats =+ 1

def change_snake(x,y, direction):
    global snake_data
    snake_data[:] = x,y, direction

def change_map_size(n, m):
    global map_size
    map_size[:] = n,m

def change_map_game(new_map):
    global map_game
    map_game[:] = new_map

