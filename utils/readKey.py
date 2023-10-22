from  readchar import readkey, key


"""while True:
    char = readchar.readchar()
    
    if char == '\xe0':  # Si se presiona la tecla de escape (inicio de secuencia de flecha)
        arrow_char = readchar.readchar()
        if arrow_char == '[':
            direction_char = readchar.readchar()
            if direction_char == 'H':
                print("Flecha hacia arriba presionada")
            elif direction_char == 'P':
                print("Flecha hacia abajo presionada")
            elif direction_char == 'M':
                print("Flecha hacia la derecha presionada")
            elif direction_char == 'K':
                print("Flecha hacia la izquierda presionada")
    elif char == 'q':
        print("Saliste")
        break"""
        
"""while True:
    char = readchar.readchar()
    if char == '\xe0H':
        print("UP")
    elif char == '\xe0P':
        print("Abajo")
    elif char == '\xe0M':
        print("derecha")
    elif char == '\xe0K':
        print("izquierda")"""


"""while True:
    char = readchar.readchar()
    print(f"Secuencia de escape: {char}")


"""

while True:
    k = readkey()
    if k == key.ENTER:
        break
    else:
        print(k)
    """elif k == key.DOWN:
        print("diwn")
    elif k == key.UP:
        print("UP")
    elif k == key.RIGHT:
        print("Right")
    elif k == key.LEFT:
        print("Left") """ 
    