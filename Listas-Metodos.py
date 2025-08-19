'''
lista = [1,2,3,4,5,6,7,8,9,10]


lista_dos = lista[3:]
print(lista_dos)

for i in range(1, 4, 2):
    print(lista[i]) 
'''

materias = ["Mate", "fisica", "progra"]   
notas = []

for materia in materias:
    nota = float(input(f"Ingrese su nota de {materia}: "))
    notas.append(nota)
    
for i in range(len(materias)):
    print(f"{materias[i]}: {notas[i]}")

