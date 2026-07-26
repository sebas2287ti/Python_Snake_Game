map_size = [10, 10]
map_game = []


fruits_eats = [0,False]


snake_data = [[1,1,"d"]]
snake_data_temporaly = [0]


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


dict_assets_snake = {
    "ww":"", "wa":"", "wd":"",
    "ss":"", "sa":"", "sd":"",
    "aa":"", "aw":"", "ws":"",
    "dd":"", "dw":"", "ds":"",
}


def change_eat_fruits():
    global fruits_eats
    fruits_eats[0] += 1
    fruits_eats[1] = True 


def change_data_snake_temporaly(new_snake_data):
    global snake_data_temporaly
    snake_data_temporaly.clear()
    print(snake_data_temporaly)
    snake_data_temporaly[:] = new_snake_data
    print(snake_data_temporaly)


def execute_movent_snake():
    pass
        

def change_map_size(n, m):
    global map_size
    map_size[:] = n,m


def change_map_game(new_map):
    global map_game
    map_game[:] = new_map
