import readchar

def greet(playerName):
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

playerName = input("Escribe tu nombre: ")
greet(playerName)

#Parte 2, proyecto integrador:
#?Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP
while True:
    k = readchar.readkey()
    if k != readchar.key.UP:
        print(k)
    else:
        print("bye")
        break


