from io import *

'''CREACION DE UN ARCHIVO'''
# Este método recibe dos parámetros: la ruta del archivo y la letra de
# acción: para este caso “w” es de write o sea escritura, “r” read de
# lectura de datos, “a” append para añadir datos.
archivo = open(r"clases/ejemplo.txt", "w")

'''ESCRITURA DE UN ARCHIVO'''
# El método write nos sirve para ingresar de cierta manera los datos.
# Este método nos recibe solo un parámetro.
archivo.write(f"\nPrueba de texto 2")
archivo.close()

'''LECTURA DE UN ARCHIVO'''
#Este método nos permite leer todo el archivo en cuestión.
archivo = open(r"clases/ejemplo.txt", "r")
lectura = archivo.read()
print(lectura)
archivo.close()
