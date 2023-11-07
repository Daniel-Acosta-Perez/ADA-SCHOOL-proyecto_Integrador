import os
import readchar


class Juego:
    def __init__(self, map_matrix, start_pos, end_pos, playerName):
        self.map_matrix = map_matrix
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.lifes = 3
        self.name = playerName

    def greet(self):
    
        print(f"""
      
       d8888      888               .d8888b.           888                        888
      d88888      888              d88P  Y88b          888                        888
     d88P888      888              Y88b.               888                        888
    d88P 888  .d88888  8888b.       "Y888b.    .d8888b 88888b.   .d88b.   .d88b.  888
   d88P  888 d88" 888     "88b         "Y88b. d88P"    888 "88b d88""88b d88""88b 888
  d88P   888 888  888 .d888888           "888 888      888  888 888  888 888  888 888
 d8888888888 Y88b 888 888  888     Y88b  d88P Y88b.    888  888 Y88..88P Y88..88P 888
d88P     888  "Y88888 "Y888888      "Y8888P"   "Y8888P 888  888  "Y88P"   "Y88P"  888

Welcome to the maze, {self.name}!

╔═══╦╗╔╦═══╦═══╦═══╦══╗╔╦═══╦══╗╔═══╗╔════╦╗─╔╦═══╦╗╔═══╦══╗
║╔═╗║║║║╔═╗║╔══╣╔═╗║╔╗║║║╔═╗║╔╗║╔═╗║║╔╗╔╗║║─║║║╔═╗║║║╔═╗║╔╗║
║╚═╝║║║║║─║║╚══╣╚═╝║║║║║║╚═╝║║║║║─║║║║║║║║╚═╝║║║─╚╝║║║─║║║║║
║╔╗╔╣║║║║─║║╔══╣╔╗╔╣║║║║║╔╗╔╣║║║║─║║║║║║║║╔═╗║║╚═╗╔╝║╚═╝║║║║
║║║╚╣╚═╝║║─║║║──║║║╚╣╚═╝║║║╚╣╚═╝║║║║║║║║─║║║╔═╝║║║╔═╗║║║║
║║║─║╔═╗║╚═╝║╚═╗║║║─║╔═╗║║║─║╔═╗║║╚═╝║║║╚═╝║║╚══╣╚╝║─║║╚═╝
╚╝╚─╚╝─╚╩═══╩══╝╚╝─╚╝─╚╩╝╚─╚╝─╚╝╚════╝╚╩═══╩══╩══╝╚══╝
""")

    def clear_screen_and_display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.map_matrix:
            print(''.join(row))
        print(f"Lifes: {self.lifes}")

    def perder_una_vida(self, px_act, py_act):
        px, py = self.start_pos
        self.map_matrix[py_act][px_act] = '.'
        self.clear_screen_and_display()
        self.map_matrix[py][px] = 'P'

    def play(self):
        px, py = self.start_pos
        is_playing = True

        while is_playing:
            self.map_matrix[py][px] = 'P'
            self.clear_screen_and_display()
            self.map_matrix[py][px] = '.'

            key = readchar.readkey()

            if key == readchar.key.UP:
                if py > 0 and self.map_matrix[py - 1][px] != '#':
                    py -= 1
                else:
                    self.lifes -= 1
                    self.perder_una_vida(px, py)
                    px, py = self.start_pos
            
            elif key == readchar.key.DOWN:
                if py < len(self.map_matrix) - 1 and self.map_matrix[py + 1][px] != '#':
                    py += 1
                else:
                    self.lifes -= 1
                    self.perder_una_vida(px, py)
                    px, py = self.start_pos

            elif key == readchar.key.LEFT:
                if px > 0 and self.map_matrix[py][px - 1] != '#':
                    px -= 1
                else:
                    self.lifes -= 1
                    self.perder_una_vida(px, py)
                    px, py = self.start_pos

            elif key == readchar.key.RIGHT:
                if px < len(self.map_matrix[0]) - 1 and self.map_matrix[py][px + 1] != '#':
                    px += 1
                else:
                    self.lifes -= 1
                    self.perder_una_vida(px, py)
                    px, py = self.start_pos


            if (px, py) == self.end_pos:
                is_playing = False
                print(f"\nCONGRATULATIONS, {self.name}, YOU ESCAPED FROM THE MAZE :) \n")
            if self.lifes <= 0:
                is_playing = False
                print(f"\nI'M SORRY, {self.name}, YOU COULDN'T ESCAPE :( \n")

def cargar_laberintos(map_dir):
    laberintos = []
    for filename in os.listdir(map_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(map_dir, filename), "r") as laberinto_file:
                laberinto_data = laberinto_file.read()
                laberintos.append(laberinto_data)
    return laberintos

def string_to_matrix(map_str):
    map_rows = map_str.split("\n")
    return [list(row) for row in map_rows]



