'''
8. Realizar un programa que haga conteo de todos los caracteres
que no sean vocales en una lista de 10 cadenas.
'''
conteo = 0
vocales = ["a", "e", "i", "o", "u"]
lista= ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp", "sistemas"]
for cadena in lista:
    for caracter in cadena.lower():  
        if caracter not in vocales:  
            conteo += 1
            
print(f"Hay {conteo} carácteres que no son vocales")