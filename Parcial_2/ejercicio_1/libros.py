'''
1. Para este punto usted debe generar un archivo JSON para crear entidades “libros”, para
esto deberá realizar las siguientes actividades:

a. Revisar la documentación respecto al tema archivo JSON que se adjuntará en la
sección del “parcial II”.

b. Analizar y documentar el archivo llamado “generador”, este algoritmo genera
archivos JSON y tiene unos datos que no concuerdan con el contexto de libros,
cosa que ustedes deben arreglar.

c. Va a generar un nuevo algoritmo donde ustedes van a adaptar el paradigma
orientado a objetos a ese código “generador”, esto quiere decir que por ejemplo
en vez de dejarlo como funciones deben diseñar métodos y así para cubrir las
necesidades del código.

d. Después de adaptar el código deberá realizar métodos para que se puedan realizar
las siguientes funcionalidades de agregar libro por consola y lectura de datos, para
este punto debe modularizar el código.
'''            
from generador import generar_json, leer_json

# class Libro:
#     def __init__(self, titulo="", autor="", anio_publicacion=None, genero="", editorial=""):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__anio_publicacion = anio_publicacion
#         self.__genero = genero
#         self.__editorial = editorial

#     def get_titulo(self):
#         return self.__titulo

#     def get_autor(self):
#         return self.__autor

#     def get_anio_publicacion(self):
#         return self.__anio_publicacion

#     def get_genero(self):
#         return self.__genero

#     def get_editorial(self):
#         return self.__editorial


#     def set_titulo(self, nuevo_titulo):
#         if isinstance(nuevo_titulo, str) and nuevo_titulo.strip(): #para verificar cadenas vacias
#             self.__titulo = nuevo_titulo.strip()
#         else:
#             raise ValueError("Titulo no valido, debe ser una cadena no vacia.")

#     def set_autor(self, nuevo_autor):
#         if isinstance(nuevo_autor, str) and nuevo_autor.strip():
#             self.__autor = nuevo_autor.strip()
#         else:
#             raise ValueError("Autor no valido, debe ser una cadena no vacia.")

#     def set_anio_publicacion(self, nuevo_anio):
#         # acepta año como entero o cadena convertible a entero razonable
#         try:
#             anio = int(nuevo_anio)
#             if anio <= 0 or anio > 2025:
#                 raise ValueError("Año no válido.")
#             self.__anio_publicacion = anio
#         except (TypeError, ValueError):
#             raise ValueError("Año no valido, ingrese un numero entero (ejemplo: 1999).")

#     def set_genero(self, nuevo_genero):
#         if isinstance(nuevo_genero, str) and nuevo_genero.strip():
#             self.__genero = nuevo_genero.strip()
#         else:
#             raise ValueError("Genero no valido, debe ser una cadena no vacia.")

#     def set_editorial(self, nueva_editorial):
#         if isinstance(nueva_editorial, str) and nueva_editorial.strip():
#             self.__editorial = nueva_editorial.strip()
#         else:
#             raise ValueError("Editorial no valida, debe ser una cadena no vacia.")

#     # ===== Entrada por consola, usando setters para validar =====
#     def agregar_libro(self):
#         while True:
#             try:
#                 titulo = input("Ingrese el título del libro: ")
#                 self.set_titulo(titulo)
#                 break
#             except ValueError as e:
#                 print(e)

#         while True:
#             try:
#                 autor = input("Ingrese el autor del libro: ")
#                 self.set_autor(autor)
#                 break
#             except ValueError as e:
#                 print(e)

#         while True:
#             try:
#                 anio = input("Ingrese el año de publicación del libro: ")
#                 self.set_anio_publicacion(anio)
#                 break
#             except ValueError as e:
#                 print(e)

#         while True:
#             try:
#                 genero = input("Ingrese el genero del libro: ")
#                 self.set_genero(genero)
#                 break
#             except ValueError as e:
#                 print(e)

#         while True:
#             try:
#                 editorial = input("Ingrese la editorial del libro: ")
#                 self.set_editorial(editorial)
#                 break
#             except ValueError as e:
#                 print(e)

#         print("\nLibro agregado exitosamente.\n")

#     def to_dict(self): #pasar a diccionario para guardar en json
#         return {
#             "titulo": self.get_titulo(),
#             "autor": self.get_autor(),
#             "anio_publicacion": self.get_anio_publicacion(),
#             "genero": self.get_genero(),
#             "editorial": self.get_editorial()
#         }

#     def guardar_libros(self, direccion_archivo):
#         libros = []
#         while True:
#             self.agregar_libro()
#             libros.append(self.to_dict())
#             continuar = input("Desea agregar otro libro? (s/n): ")
#             if continuar.lower() != "s":
#                 break
            
#         generar_json(direccion_archivo, libros)
#         print(f"\nSe guardaron {len(libros)} libros en {direccion_archivo}")

#     # ===== Cargar y mostrar =====
#     def cargar_libros(self, direccion_archivo):
#         libros = leer_json(direccion_archivo) 
#         if libros:
#             print("\n---LISTA DE LIBROS---")
#             for i, libro in enumerate(libros, start=1):
#                 print(f"{i}. {libro.get('titulo')} | {libro.get('autor')} | {libro.get('anio_publicacion')} | {libro.get('genero')} | {libro.get('editorial')}")
#         else:
#             print("No se pudieron cargar los libros o el archivo está vacío.")
            
            
            
class Libro:
    def __init__(self, titulo="", autor="", anio_publicacion="", genero="", editorial=""):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__genero = genero
        self.__editorial = editorial

    def get_titulo(self): 
        return self.__titulo
    
    def get_autor(self): 
        return self.__autor

    def get_anio_publicacion(self): 
        return self.__anio_publicacion

    def get_genero(self): 
        return self.__genero
    
    def get_editorial(self): 
        return self.__editorial

    def agregar_libro(self):
        self.__titulo = input("Ingrese el título del libro: ")
        self.__autor = input("Ingrese el autor del libro: ")
        self.__anio_publicacion = input("Ingrese el año de publicación del libro: ")
        self.__genero = input("Ingrese el género del libro: ")
        self.__editorial = input("Ingrese la editorial del libro: ")
        print("\nLibro agregado exitosamente.")

    #convertir a diccionario para guardar en JSON
    def to_dict(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "anio_publicacion": self.__anio_publicacion,
            "genero": self.__genero,
            "editorial": self.__editorial
        }

    def guardar_libros(self, direccion_archivo):
        libros = []
        while True:
            self.agregar_libro()
            libros.append(self.to_dict())
            continuar = input("Desea agregar otro libro? (s/n): ")
            if continuar.lower() != "s":
                break
            
        generar_json(direccion_archivo, libros)
        print(f"\nSe guardaron {len(libros)} libros en {direccion_archivo}")

    # Cargar libros desde el archivo JSON
    def cargar_libros(self, direccion_archivo):
        libros = leer_json(direccion_archivo)
        if libros:
            print("\n---Lista de libros guardados---")
            for libro in libros:
                print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, "
                      f"Año: {libro['anio_publicacion']}, Genero: {libro['genero']}, "
                      f"Editorial: {libro['editorial']}")
        else:
            print("No se pudieron cargar los libros o el archivo está vacío.")

