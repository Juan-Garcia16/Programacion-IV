'''
10. Elabore un programa para ingresar la siguiente lista.
Lista= [“casa”, “programación”, “utp”, “universidad”, “utp, “casa”,
“casa”,” thj”, “vbh”, “456”, “987”]
a. Borre los elementos repetidos que tengamos en la lista
b. Borre las cadenas que NO contengan vocales.
c. Ordene la lista en orden alfabético respecto al primer
elemento de la cadena.
'''
lista = ["casa", "programación", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]
vocales = ["a", "e", "i", "o", "u"]

for repetido in lista:
    cantidad = lista.count(repetido)
    if cantidad > 1:
        for i in range (cantidad):
            lista.remove(repetido)
print("Lista sin repetidos:")
print(lista)

nueva_lista = []
for palabra in lista:
    for vocal in vocales:
        if vocal in palabra.lower():
            nueva_lista.append(palabra)
            break   
print("Lista sin cadenas que no contienen vocales:")
print(nueva_lista)

nueva_lista.sort()
print("Lista ordenada alfabéticamente:")
print(nueva_lista)


            
