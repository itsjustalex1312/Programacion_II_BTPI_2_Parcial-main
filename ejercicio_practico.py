# Pseudocodigo
# Solicitar el total de la compra del usuario y guardarla en una variable llamada "total_compra"
# Si la variable "total_compra" es mayor a 2000:
#   Crear una variable llamada "descuento" que contenga la mulriplicacion de las variables "total_compra" y "0.08"
#   Imprimir por consola el texto "el descuento es de < descuento >"
# Caso contrario:
#   Inprimir por consola el texto "no aplica"

# Codigo

total_compra = int(input("Ingrese el total de su compra "))

if(total_compra > 2000):
    descuento = total_compra * 0.08
    print("El descuento es de " + str(descuento))
else:
    print("no aplica ")

