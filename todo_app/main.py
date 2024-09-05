from menu import imprimir_menu
from datos import crear_tarea,obtener_todas_las_tareas, eliminar_tarea, obtener_tareas_pendientes, obtener_tareas_completadas, completar_tarea
#import json

salir = False

#with open('test.json') as testF:
 #   texto = testF.read()
 #   print(texto)
#
 #   data = json.loads(texto)
 #   print(data)
 #   print(data['usuarios'])


#test_data= {
#    'texto': 'Hola Mundo',
#    'estado': True,
#    'valor': 3.1
#}
#
#print(test_data)
#
#json_text = json.dumps(test_data)
#print(json_text)
#
#with open('datos.json','w') as datos_file:
#    datos_file.write(json_text)
#    datos_file.close()
#si se utiliza open sin ningun argumento, este leera en modo lectura

while not salir:
    imprimir_menu()
    resp = input("Ingrese una opcion: ")

    if resp =='0':
        salir = True
    elif resp == '1':
        print('\n------ Todas las Tareas------')
        Tareas = obtener_todas_las_tareas()
        for Tarea in Tareas:
            index = Tareas.index(Tarea)
            print(f'{index + 1}. {Tarea['titulo']}')
    elif resp == '2':
         print('\n------Tareas Pendientes------')
         Tareas = obtener_tareas_pendientes()
         for Tarea in Tareas:
            index = Tareas.index(Tarea)
            print(f'{index + 1}. {Tarea['titulo']}')
    elif resp == '3':
         print('\n------Tareas Completadas------')
         Tareas = obtener_tareas_completadas()
         for Tarea in Tareas:
            index = Tareas.index(Tarea)
            print(f'{index + 1}. {Tarea['titulo']}')
    elif resp == '4':
        titulo_tarea = input('ingrese la nueva tarea: ')
        crear_tarea(titulo_tarea)
        print('\nTarea Agregada!\n\n')
    elif resp == '5':
        print('\n------ Todas las Tareas------')
        Tareas = obtener_todas_las_tareas()
        for Tarea in Tareas:
            index = Tareas.index(Tarea)
            print(f'{index + 1}. {Tarea['titulo']}') 
        del_opt = input("Ingrese el numero de la tarea que desea eliminar: ")

        del_index = int(del_opt) - 1

        del_tarea = Tareas[del_index]

        eliminar_tarea(del_tarea)

        print('\nTarea Eliminada!\n\n')
    
    elif resp == '6':
        print('\n----- Completar una tarea -----')
        tareas = obtener_tareas_pendientes()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1}, {tarea['titulo']}')
        
        comp_opt = input("ingrese el numero de la tarea que desea completar: ")

        comp_index = int(comp_opt) - 1

        comp_tarea = tareas[comp_index]
        
        completar_tarea(comp_tarea['id'])

        print('\nTarea Completada!\n\n')
    else:
        print(f"la opcion '{resp}' no es valida ")