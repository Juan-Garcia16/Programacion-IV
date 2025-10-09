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
        while not self.__anio_publicacion.isdigit() or len(self.__anio_publicacion) != 4 or int(self.__anio_publicacion) > 2025:
            print("Año de publicación inválido. Por favor, ingrese un año válido (4 dígitos).")
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
        libros_existentes = leer_json(direccion_archivo)
        if not libros_existentes:
            libros_existentes = []  

        while True:
            self.agregar_libro()
            libros_existentes.append(self.to_dict())
            continuar = input("¿Desea agregar otro libro? (s/n): ")
            if continuar.lower() != "s":
                break

        generar_json(direccion_archivo, libros_existentes)
        print(f"\nSe guardaron {len(libros_existentes)} libros en {direccion_archivo}")

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

