'''
9. Realizar un programa que inicialice una lista con 15 valores
aleatorios y posteriormente muestre en pantalla cada elemento
de la lista junto con su cuadrado y su cubo.
'''
import random

lista = [random.randint(1, 50) for i in range(15)]

print(f"Lista generada: {lista}\n")
for numero in lista:
    print(f"Número: {numero}, cuadrado: {numero ** 2}, cubo: {numero ** 3}")