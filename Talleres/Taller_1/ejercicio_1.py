'''
1. Realice un algoritmo para sumar los valores numéricos de la
siguiente lista sin ordenarla:
Lista = [2, 8,” hola”, “programación”, 10, “utp”, 85, 82, 100, ”mundo”]
'''
lista = [2, 8, "hola", "programación", 10, "utp", 85, 82, 100, "mundo"]
numeros =[numero for numero in lista if type(numero) == int]
suma = sum(numeros)
print("La suma de los valores númericos en la lista es:", suma)



