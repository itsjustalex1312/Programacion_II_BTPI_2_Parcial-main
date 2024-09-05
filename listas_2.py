

salir = False
Lista_Compras = []

while not salir:
    print("------ Menu ------")
    print("1. Imprimir Lista de Compras")
    print("2. Agregar elememto a lista")
    print("0. Salir")

    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir =True
    elif(opt == '1'):
        print("------ Lista de Compras ------")

        for i in range(len(Lista_Compras)):
            print(f"{i + 1}. {Lista_Compras[i]}")
    elif(opt == '2'):
        nuevo_elemento = input("Ingrese el nombre del producto: ")
        # print(nuevo_elemento)
        Lista_Compras.append(nuevo_elemento)
        print(f"El elemento ya esta en la lista: {nuevo_elemento}")
        # print(f"El elemento'{nuevo_elemento}' fue agregado a la lista.")
    else:
        print("Opcion no valida!")