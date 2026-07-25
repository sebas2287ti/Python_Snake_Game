from snake_game.state import map_size, map_game, change_map_game, snake_data 
import os

def create_map():
    n, m = map_size
    map_create_game = []

    for x in range(n):
        fila = []
        for y in range(m):
            fila.append(0)
        map_create_game.append(fila)

    y,x,direction = snake_data
    map_create_game[y][x] = direction
    
    change_map_game(map_create_game)

def print_map():
    os.system("cls")

    for x in map_game:
        print("| ", end="")
        for y in x:
            print(y, " ", end="")
        print("|")





