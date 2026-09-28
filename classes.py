import json
from pathlib import Path

# Obtener el archivo de json.
archivo = Path(__file__).parent / "datos" / "classes.json"
with archivo.open("r", encoding="utf-8") as f:
    datos = json.load(f)

clases = datos

def agregar_clase():
    # Usuario
    num = input('ID: ')
    nombre_c = input('Nombre: ')
    

    if num in datos:
        print("Este id de clase ya está registrado")
        return
    else:
        clases[num] = {
            'nombre_c': nombre_c,
            'students': {}
        }

        with archivo.open("w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
    return print('Clase agregada')

def agregar_ligadura():
    id_clase = input('Id de la clase: ')
    id_ligadura = input('Id de la ligadura: ')
    id_estudiante = input('Id del estudiante ligado: ')

    if id_clase not in clases:
       print(f"No existe la clase {id_clase}")
       return
    
    estudiantes = clases[id_clase].setdefault("students", {})

    if id_ligadura in estudiantes:
        print(f"Ya existe la ligadura {id_ligadura}")
        return

    students = clases[id_clase]["students"]

    # Vamos a reutilizar esto de aquí items().
    for id_ligadura2, id_estudiante2 in students.items():
        if id_estudiante2 == id_estudiante:
            print(f"Este estudiante ya está con la ligadura {id_ligadura2}.")
            return

    estudiantes[id_ligadura] = id_estudiante


    with archivo.open("w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)  

def eliminar_clase():
    num = input('Id de clase: ')

    if num not in clases:
        print('Esta clase no existe.')
        return

    del clases[num]

    with archivo.open("w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

    print('Clase eliminada con éxito.')

def editar_nombre_clase():
    ID_c = input('Id de la clase: ')
    nombre = input('Nuevo nombre: ')
    if ID_c not in clases:
        print('Esta clase no existe.')
        return

    clases[ID_c]["nombre_c"] = nombre

    with archivo.open("w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2) 

def mostrar_clases():
    for e in datos:
        nombre = clases[e]["nombre_c"]
        estudiante = clases[e]["students"]
        print(f'Nombre: {nombre} \n estudiantes: {estudiante}')


