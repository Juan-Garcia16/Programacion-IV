'''
7. Realizar un programa que pida al usuario un carácter, luego se
debe mostrar las cadenas que contengan dicho carácter y debe
mostrar si dichas cadenas son pares o impares.
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”,”
objetos”, “listas”, “métodos”, “utp”]
'''
lista= ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp"]
caracter = input("Ingrese un carácter: ")
for cadena in lista:
    if caracter in cadena:
        print(cadena, "|", end=" ")
        if len(cadena) % 2 == 0:
            print("par")
        else:
            print("Impar")