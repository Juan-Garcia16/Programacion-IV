'''
6. Realice un programa en el que el usuario ingrese un valor
entero, luego debe mostrar en pantalla las cadenas cuya longitud
sea igual al número ingresado, puede usar la lista del ejercicio 5
o 7.
'''
lista= ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp"]

longitud = int(input("Ingrese un número entero positivo: "))
encontrado = False

for cadena in lista:
    if len(cadena) == longitud:
        print(cadena)
        encontrado = True
        
if not encontrado:
    print("No hay cadenas con esa longitud")