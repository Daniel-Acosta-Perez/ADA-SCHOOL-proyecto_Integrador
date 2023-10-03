import readchar
def readKey():
    print("Presiona teclas. Termina con flecha ARRIBA")

    while True:
        key = readchar.readkey()
  
        if key == "\x1b[A":
            print("UP") 
            break
  
        print(key)

    print("Has terminado")