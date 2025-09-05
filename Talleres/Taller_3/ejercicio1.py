'''
Cree una clase llamada `Libro` con atributos como título, autor, año, editorial y
género. Incluya métodos para mostrar la información del libro, guardar los datos en un
archivo y buscar libros por autor.
'''
class Libro:
    def __init__(self, titulo, autor, año, editorial, genero):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.editorial = editorial
        self.genero = genero
    
    def __str__(self):
        return f"{self.titulo},{self.autor},{self.año},{self.editorial},{self.genero}"

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
        print(f"Editorial: {self.editorial}")
        print(f"Género: {self.genero}")

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(str(self) + '\n')

    def buscar_por_autor(nombre_archivo, autor):
        libros = []
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                if datos[1].lower() == autor.lower():
                    libros.append(datos)
        return libros
    
libros = [
    Libro("El bosque perdido", "Juan Perez", 2001, "Editorial Sol", "Fantasia"),
    Libro("La casa de piedra", "Maria Lopez", 1995, "Luz y Letras", "Drama"),
    Libro("Camino al mar", "Pedro Ramirez", 2010, "Oceano Azul", "Aventura"),
    Libro("Noche eterna", "Laura Gomez", 2018, "Estrella Norte", "Suspenso"),
    Libro("Sombras en la arena", "Carlos Torres", 2022, "Editorial Horizonte", "Misterio"),
    Libro("El eco de las montañas", "Juan Perez", 2005, "Editorial Sol", "Fantasia"),
    Libro("El guardián del valle", "Juan Perez", 2012, "Editorial Sol", "Aventura"),
    Libro("Sombras de medianoche", "Laura Gomez", 2020, "Estrella Norte", "Suspenso"),
    Libro("La bruma del amanecer", "Carlos Torres", 2019, "Editorial Horizonte", "Misterio"),
]


for libro in libros:
    libro.guardar_en_archivo('libros.txt')
    libro.mostrar_info()
    print()

while True:
    autor = input("Ingrese el nombre de un autor para buscar sus libros: ")
    resultados = Libro.buscar_por_autor('libros.txt', autor)
    
    if resultados:
        print("Libros encontrados:")
        for libro in resultados:
            print(f"Título: {libro[0]}, Autor: {libro[1]}, Año: {libro[2]}, Editorial: {libro[3]}, Género: {libro[4]}")
    else:
        print("No se encontraron libros del autor especificado.")
        
    continuar = input("Desea buscar otro autor? (s/n): ")
    if continuar.lower() == 's':
        pass
    elif continuar.lower() == 'n':
        print("Saliendo del programa")
        break
    else:
        print("Opción no valida. Saliendo del programa")
        break
    