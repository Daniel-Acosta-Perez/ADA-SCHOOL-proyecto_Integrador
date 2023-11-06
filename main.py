import os
import random
import readchar
import time
from Laberintos import lista_laberintos, lista_laberintos2


def greet():
    playerName = input("Escribe tu nombre: ")
    print(f"""
      
       d8888      888               .d8888b.           888                        888
      d88888      888              d88P  Y88b          888                        888
     d88P888      888              Y88b.               888                        888
    d88P 888  .d88888  8888b.       "Y888b.    .d8888b 88888b.   .d88b.   .d88b.  888
   d88P  888 d88" 888     "88b         "Y88b. d88P"    888 "88b d88""88b d88""88b 888
  d88P   888 888  888 .d888888           "888 888      888  888 888  888 888  888 888
 d8888888888 Y88b 888 888  888     Y88b  d88P Y88b.    888  888 Y88..88P Y88..88P 888
d88P     888  "Y88888 "Y888888      "Y8888P"   "Y8888P 888  888  "Y88P"   "Y88P"  888

Welcome to the maze, {playerName}!

╔═══╦╗╔╦═══╦═══╦═══╦══╗╔╦═══╦══╗╔═══╗╔════╦╗─╔╦═══╦╗╔═══╦══╗
║╔═╗║║║║╔═╗║╔══╣╔═╗║╔╗║║║╔═╗║╔╗║╔═╗║║╔╗╔╗║║─║║║╔═╗║║║╔═╗║╔╗║
║╚═╝║║║║║─║║╚══╣╚═╝║║║║║║╚═╝║║║║║─║║║║║║║║╚═╝║║║─╚╝║║║─║║║║║
║╔╗╔╣║║║║─║║╔══╣╔╗╔╣║║║║║╔╗╔╣║║║║─║║║║║║║║╔═╗║║╚═╗╔╝║╚═╝║║║║
║║║╚╣╚═╝║║─║║║──║║║╚╣╚═╝║║║╚╣╚═╝║║║║║║║║─║║║╔═╝║║║╔═╗║║║║
║║║─║╔═╗║╚═╝║╚═╗║║║─║╔═╗║║║─║╔═╗║║╚═╝║║║╚═╝║║╚══╣╚╝║─║║╚═╝
╚╝╚─╚╝─╚╩═══╩══╝╚╝─╚╝─╚╩╝╚─╚╝─╚╝╚════╝╚╩═══╩══╩══╝╚══╝
""")

# Convierte el mapa en una matriz de caracteres
def string_to_matrix(map_str):
    map_rows = map_str.split("\n")
    return [list(row) for row in map_rows]

# Función para limpiar la pantalla y mostrar la matriz
def clear_screen_and_display(matrix, lifes):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in matrix:
        print(''.join(row))
    print(f"Lifes: {lifes}")

def perder_una_vida(Lifes, start_pos, map_matrix, px_act, py_act):
    px, py = start_pos
    map_matrix[py_act][px_act] = '.'
    clear_screen_and_display(map_matrix, Lifes)
    map_matrix[py][px] = 'P'
    return map_matrix

# Bucle principal del juego
def play(map_matrix, start_pos, end_pos):
    px, py = start_pos
    Lifes = 3
    is_playing = True

    while is_playing:
        map_matrix[py][px] = 'P'
        clear_screen_and_display(map_matrix, Lifes)
        map_matrix[py][px] = '.'

        key = readchar.readkey()  #Leer una tecla
        if key == readchar.key.UP:
            if py > 0 and map_matrix[py - 1][px] != '#':
                py -= 1
            else:
                Lifes -= 1
                map_matrix = perder_una_vida(Lifes, start_pos, map_matrix, px, py)
                px, py = start_pos

        elif key == readchar.key.DOWN:
            if py < len(map_matrix) - 1 and map_matrix[py + 1][px] != '#':
                py += 1
            else:
                Lifes -= 1
                map_matrix = perder_una_vida(Lifes, start_pos, map_matrix, px, py)
                px, py = start_pos

        elif key == readchar.key.LEFT:
            if px > 0 and map_matrix[py][px - 1] != '#':
                px -= 1
            else:
                Lifes -= 1
                map_matrix = perder_una_vida(Lifes, start_pos, map_matrix, px, py)
                px, py = start_pos

        elif key == readchar.key.RIGHT:
            if px < len(map_matrix[0]) - 1 and map_matrix[py][px + 1] != '#':
                px += 1
            else:
                Lifes -= 1
                map_matrix = perder_una_vida(Lifes, start_pos, map_matrix, px, py)
                px, py = start_pos
        
        if (px, py) == end_pos:
            is_playing = False
            print("GANASTE")
        if Lifes <= 0:
            is_playing = False
            print("PERDISTE")

# Convertir el mapa en una matriz
mapa = string_to_matrix(random.choice(lista_laberintos2))

# Coordenadas iniciales y finales
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0]) - 1, len(mapa)-1)

greet()
time.sleep(2)

# Ejecutar el bucle principal del juego
play(mapa, posicion_inicial, posicion_final)
