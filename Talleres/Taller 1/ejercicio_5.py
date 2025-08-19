'''
5. Realice un programa que almacene una cantidad de cadenas
dictaminadas por el usuario, en pantalla se debe mostrar la
cadena que más caracteres contenga y la cadena que menos
caracteres contenga.
Ejemplo:
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”]
Cadena mayor = programación.
Cadena menor = oso
'''
cadenas = []

cantidad = int(input("Cuantas cadenas desea ingresa?: "))
print(f"Ingrese las {cantidad} cadenas:")
for cadena in range(cantidad):
    cadena = input()
    cadenas.append(cadena)
    
cadena_mayor = ""
cadena_menor = cadenas[0]

for cadena in cadenas:
    if len(cadena_mayor) < len(cadena):
        cadena_mayor = cadena
    if len(cadena_menor) > len(cadena):
        cadena_menor = cadena
  
print("Cadena mayor:", cadena_mayor)
print("Cadena menor:", cadena_menor)

# IMPORTANTES
# cadena_mayor = max(cadenas, key=len)
# cadena_menor = min(cadenas, key=len)