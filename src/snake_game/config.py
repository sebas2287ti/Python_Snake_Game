import os

map_size = (10, 10)

class MapTooSmallError(Exception):
     pass

def create_map():

    creation_valid = True
    while creation_valid:
        try:
            n = int(input("Ingresa una cantidad mayor a 3 filas para el mapa: "))
            m = int(input("ingresa una cantidad mayor a 3 columnas para el mapa: "))

            if (n <= 3 or m <= 3):
                raise MapTooSmallError("numero menor a 3.")

        except MapTooSmallError:
                print("El mapa es muy pequeño para poder jugar.")
                input()

        except: 
                print("Solo se permiten numeros.")
                input()

        else:
            creation_valid = False
            global map_size 
            map_size = (n, m)

        finally:
            os.system("cls")

    return map_size
        
