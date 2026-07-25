from snake_game.config import map_size
import os

map_game = []

def create_map():
    n, m = map_size
    map_game = []

    for x in range(n):
        fila = []
        for y in range(m):
            fila.append(0)
        map_game.append(fila)
    return map_game

def print_map(map_game):
    os.system("cls")

    for x in map_game:
        print("| ", end="")
        for y in x:
            print(y, " ", end="")
        print("|")

dict_direction = { 
    "a":(0,-1),
    "w":(-1,0),
    "s":(1,0),
    "d":(0,1)
}



