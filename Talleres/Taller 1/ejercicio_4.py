'''
4. Escriba un programa que pida al usuario la cantidad que desea
de la lista, luego el usuario debe ingresar valores numéricos
enteros hasta llenar la lista, luego de ingresarlos se debe
imprimir en pantalla cada número ingresado por el usuario y al
lado debe aparecer ese mismo número al cuadrado y al lado ese
mismo número al cubo, ejemplo:
L = [2,3]
Salida:
2 - 4 - 8
3 - 9 - 27
'''
numeros = []
cantidad = int(input("Cuántos valores desea ingresar?: "))
print("Ingrese los valores:")
for numero in range(cantidad):
    numero = int(input())
    numeros.append(numero)
for numero in numeros:
    print(f"{numero} - {numero**2} - {numero**3}")