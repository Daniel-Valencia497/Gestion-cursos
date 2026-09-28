import json
from pathlib import Path
import students
import classes

# Obtener el archivo de json.
archivo = Path(__file__).parent / "datos" / "datos.json"
with archivo.open("r", encoding="utf-8") as f:
    datos = json.load(f)


# Bucle de interracción.
print('OS para administrar estudiantes y OC para administrar clases. \n')

while True:
    user_ = input(':: ')

    valido = ['OS', 'OC', 'salir']

    if user_ not in valido:
        print('Establece un valor válido: OS, OC o salir')
    
    if user_ == 'salir':
        exit()

    while user_ == 'OS':
        print('Administrador de estudiantes \n 0. Salir del programa. \n 1. Ver instrucciones.')
        instrucciones = '''
        2. Añadir un nuevo estudiante,
        3. Eliminar un estudiante,
        4. Editar información de un estudiante,
        5. Buscar información de un estudiante
        (nota: solo números puedes usar en esta parte)
        6. Ver todos los estudiantes.
    '''
        user = int(input(':: '))
        if user == 0:
            break
        if user == 1:
            print(instrucciones)
        if user == 2:
            students.agregar_estudiante()
        if user == 3:
            students.eliminar_estudiante()
        if user == 4:
            students.editar_estudiante()
        if user == 5:
            students.buscar_estudiante()
        if user == 6:
            students.visualizar_estudiantes()
    
    while user_ == 'OC':
        print('Administrador de clases: \n 0. Salir del programa \n 1. Ver instrucciones')
        instrucciones = '''
        2. Añadir clase
        3. Añadir nueva ligadura
        4. Eliminar una clase
        5. Editar el nombre de una clase
        6. Mostrar todas las clases
    '''
        user = int(input(':: '))
        if user == 0:
                break
        if user == 1:
            print(instrucciones)
        if user == 2:
            classes.agregar_clase()
        if user == 3:
            classes.agregar_ligadura()
        if user == 4:
            classes.eliminar_clase()
        if user == 5:
            classes.editar_nombre_clase()
        if user == 6:
            classes.mostrar_clases()
    