

salir = False

while not salir:
    print("------ Menu ------")
    print("1. Suma")
    print("2. Resta")
    print("3. Divicion")
    print("4. Multiplicacion")
    print("0. Salir")
    
    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    
    elif(opt == '1'):
        numero1 = int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese otro numero: "))

        resultado = numero1 + numero2

        print("El resultado de la suma es: " + str(resultado))
    
    elif(opt == '2'):
        numero1 = int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese otro numero: "))

        resultado = numero1 - numero2

        print("El resultado de la resta es: " + str(resultado))
    
    elif(opt == '3'):
        numero1 = int(input("Ingrese un numero: "))
        numero2 = int(input("Ingrese otro numero: "))

        resultado = numero1 / numero2

        print("El resultado de la divicion es: " + str(resultado))
    
    elif(opt == '4'):
      numero1 = int(input("Ingrese un numero: "))
      numero2 = int(input("Ingrese otro numero: "))

      resultado = numero1 * numero2

      print("El resultado de la multiplicacion es: " +str(resultado))
    
    else:
        print("Opcion no valida!")