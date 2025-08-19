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
cantidad_materias = int(input("Cuántas materias desea ingresar?: "))
print("Ingrese el nombre de cada materia")

for materia in range(cantidad_materias):
    materia = input("Materia: ")
    materias.append(materia)
    
    print(f"Ingrese las 4 notas de {materia}.")
    for nota in range(4):
        nota = float(input())
        
       

print(materias)
#print(notas_materias)