

salir = False

while not salir:
    print("------ Menu ------")
    print("1. Imprimir tabla")
    print("0. Salir")

    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir =True
    elif(opt == '1'):
        tabla = int(input("Ingrese la tabla que desea Iprimir: "))

        print(f"***** tabla del {tabla} *****")
        for i in range(1,11):
            print(f"{tabla} x {i} = {tabla*i}")
    else:
        print("Opcion no valida!")