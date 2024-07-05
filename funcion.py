import random
import csv

def registar(lista:list):
    ID = random.randint(10000, 100000)
    contador_v = 0
    contador_s = 0
    contador_d = 0

    print("***DATOS DEL JUGADOR***")
    while True:
        nombre = input("Nombre: ")
        if nombre.isalpha():
            break
        else:
            print("Solo Letras.")
            continue

    while True:
        edad = int(input("Edad: "))
        if edad > 0:
            break
        else:
            print("Edad debe ser mayor a 0")
            continue
    
    while True:         
        equipo = input("Equipo: ").lower()
        if equipo.isalpha():
            break
        else:
            print("Solo Letras.")
            continue

    print("Tazas de café")
    while True:
        dia_v = int(input("Viernes: "))
        contador_v += dia_v
        dia_s = int(input("Sabado: "))
        contador_s += dia_s
        dia_d = int(input("Domingo: "))
        contador_d += dia_d
            
        total = contador_v + contador_s + contador_d
        if total >= 3:
            break
        else: 
            print(f"Cantidad de taza debe ser superior a 3, tus tazas {total}")
            continue

    lista.append([ID, nombre, edad, equipo, dia_v, dia_s, dia_d])
def listar_consumo(lista):
    print("ID Consumo\tJugador\t  Edad\t  Equipo\t   Viernes\t  Sabado\t  Domingo")
    for i in lista:
        print(f"{i[0]}         \t{i[1]}\t{i[2]}\t{i[3]}       \t{i[4]}        \t{i[5]}       \t{i[6]}")

def imprimir_consumo(lista):
    while True:
        equipo = input("Ingresa el nombre del equipo: ").lower()
        if equipo.isalpha():
            break
        else:
            print("Solo Letredas.")
            continue

    
    archivo =  open("Imprimir.csv", "w")
    archivo.write("ID Consumo\tJugador\t  Edad\t  Equipo\t   Viernes\t  Sabado\t  Domingo\n")
    for i in lista:
        if equipo == i[3]:
             archivo.write(f"{i[0]}         \t{i[1]}\t{i[2]}\t{i[3]}       \t{i[4]}        \t{i[5]}       \t{i[6]}")
        elif equipo == "todos":
            archivo.write(f"{i[0]}         \t{i[1]}\t{i[2]}\t{i[3]}       \t{i[4]}        \t{i[5]}       \t{i[6]}")
        
def buscar_consumo(lista):
    while True:
        ID = int(input("Ingresa ID que quieres buscar: "))
        for i in lista:
            if ID == i[0]:
                print("ID Consumo\tJugador\t  Edad\t  Equipo\t   Viernes\t  Sabado\t  Domingo")
                print(f"{i[0]}         \t{i[1]}\t{i[2]}\t{i[3]}       \t{i[4]}        \t{i[5]}       \t{i[6]}")
                break
            else:
                print("ID ingresado no valido, vuelva a intentar.")
                continue

                

