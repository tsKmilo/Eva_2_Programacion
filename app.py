import funcion as f

listado_consumo = []

while True:
    print("1. Registar")
    print("2. Listar Consumo")
    print("3. Imprimir consumo")
    print("4. Buscar consumo")
    print("5. SALIR.")

    opc = input("Ingresa opción: ")
    

    if opc == "1":
        f.registar(listado_consumo) 

    elif opc == "2":
        f.listar_consumo(listado_consumo)

    elif opc == "3":
        f.imprimir_consumo(listado_consumo)

    elif opc == "4":
        f.buscar_consumo(listado_consumo)

    elif opc == "5":
        print("SALIENDO...")
        break

    else:
        print("Opcion ingresada no valida, intente nuevamente.")
        continue