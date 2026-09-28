import json
from pathlib import Path


# Obtener el archivo de json.
archivo = Path(__file__).parent / "datos" / "datos.json"
with archivo.open("r", encoding="utf-8") as f:
    datos = json.load(f)

def agregar_estudiante():
    # Usuario
    num = input('ID: ')
    nombre = input('Nombre: ')
    edad = int(input('Edad: '))

    if num in datos:
        print("Este id de estudiante ya está registrado")
        return
    else:
        datos[num] = {
            'nombre': nombre, 'edad': edad
        }

        with archivo.open("w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
    return print('Estudiante agregado')

def eliminar_estudiante():
    # Usuario
    num = input('ID: ')

    if num not in datos:
        print('Este estudiante no existe')
        return
    del datos[num]

    with archivo.open("w", encoding="utf-8") as d:
        json.dump(datos, d, ensure_ascii=False, indent=2)

def editar_estudiante():
    # Usuario
    num = input('ID: ')
    name = input('Nombre: ')
    age = input('Edad: ')

    if num not in datos:
        print('Este estudiante no se encuetra')
        return

    datos[num] = {
        'nombre': name, 'edad': age 
    }

    with archivo.open("w", encoding="utf-8") as c:
        json.dump(datos, c, ensure_ascii=False, indent=2)

def buscar_estudiante():
    # User
    id = input('ID: ')
    if id not in datos:
        print('EL estudiante no existe o el comando está mal escrito.')
        return
    estudiante = f'Nombre: {datos[id]["nombre"]} \n Edad: {datos[id]["edad"]}'
    print(f'Estudiante encontrado, \n {estudiante}')
    return

def visualizar_estudiantes():
    for student in datos:
        nombre = "nombre"
        edad = 'edad'
        ID = student
        print(f'Nombre: {datos[student][nombre]}, \n Edad: {datos[student][edad]}\n')
