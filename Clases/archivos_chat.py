from io import *
# CREACIÓN Y ESCRITURA
with open("clases/ejemplo.txt", "w") as archivo:
    archivo.write("Prueba de texto 2\n")

# LECTURA
with open("clases/ejemplochat.txt", "r") as archivo:
    lectura = archivo.read()

print("Contenido del archivo:", lectura)
