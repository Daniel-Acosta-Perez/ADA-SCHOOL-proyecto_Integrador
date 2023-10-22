import os
import readchar

num = 0 

def imprimir_numero():
    os.system('cls' if os.name=='nt' else 'clear')
    print(num)

print("Presione la tecla n")
while num <= 50:
    k = readchar.readkey().lower() #Leemos la tecla presionada y la convertimos en minuscula
    if k == "n":
        imprimir_numero()
        num += 1
    else:
        print("Presione la tecla n")