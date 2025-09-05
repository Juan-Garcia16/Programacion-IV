'''
3. Escribir un programa que almacene las asignaturas de un curso
en una lista, pida al usuario las 4 notas de cada materia y en
pantalla mostrar el promedio que ha sacado en cada materia y si
alguna materia queda por debajo de la nota 3 debe salir en
pantalla “asignatura perdida”, luego se deben calcular el
promedio general de todas las materias si el promedio está por
debajo de 3 debe imprimir “semestre perdido”, si esta entre 3 y 4
debe imprimir “buen trabajo”, si el promedio esta entre 4 y 5
debe imprimir “felicidades serás becado”.
Salida de datos:
Matemáticas - nota1: 2, nota2: 2, nota3: 2, nota 4: 2
Promedio de matemáticas: 2 - asignatura perdida
Inglés - nota1: 3, nota2: 3, nota3: 3, nota 4: 3
Promedio de matemáticas: 3 - asignatura ganada
Promedio general: 2.5 - “Semestre perdido”
'''
materias = []
promedios_materias = []

print("\tGestión Académica")
cantidad_materias = int(input("Cuantas materias desea ingresar?: "))
print("Ingrese el nombre de cada materia:")

for i in range(cantidad_materias):
    materia = input("Materia: ")
    materias.append(materia)
    
    notas = []
    print(f"Ingrese las 4 notas de {materia}:")
    for i in range(4):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)
    
    promedio = sum(notas) / len(notas)
    promedios_materias.append(promedio)
    
    print(f"materia -", end=" ")
    for i in range(4):
        print(f"nota{i + 1}: {notas[i]}", end=" ")
    print("\n")
    if promedio < 3:
        print(f"Promedio de {materia}: {round(promedio, 2)} - asignatura perdida")
    else:
        print(f"Promedio de {materia}: {round(promedio, 2)} - asignatura ganada")
    print("-" * 40)

promedio_general = sum(promedios_materias) / len(promedios_materias)
print(f"Promedio general: {round(promedio_general, 2)}")

if promedio_general < 3:
    print("Semestre perdido")
elif 3 <= promedio_general < 4:
    print("Buen trabajo")
else:
    print("Felicidades serás becado!")