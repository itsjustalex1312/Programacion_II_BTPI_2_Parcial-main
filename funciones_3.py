

def crear_usuario(nombre:str, apellido:str, f_nac:str, estado:bool=True):
    if nombre == 'Alex':
        print('El nombre es Alex')
        
    nuevo_usuario = {
        'nombre': nombre,
        'apellido': apellido,
        'f_nac': f_nac,
        'estado': estado
        }

    return nuevo_usuario


usuario_1 = crear_usuario('David','Vargas','22/08/2007')
usuario_2 = crear_usuario('Abigail','Vargas','11/07/2000', False)

print(usuario_1)
print(usuario_2)
