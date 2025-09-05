'''
5. Cree una clase `Encuesta` que almacene respuestas de usuarios (edad, género,
ciudad, opinión). Guarde cada respuesta en un archivo distinto por ciudad. Muestre
estadísticas por género.
'''
class Encuesta:
    def __init__(self, edad, genero, ciudad, opinion):
        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad
        self.opinion = opinion
        
    def __str__(self):
        return f"{self.edad},{self.genero},{self.ciudad},{self.opinion}"
    
    def guardar_por_ciudad(self):
        nombre_archivo = f"encuesta_{self.ciudad}.txt"
        with open(nombre_archivo, "a") as archivo:
            archivo.write(str(self) + "\n")
    
    def estadisticas_por_genero(self):
        nombre_archivo = f"encuesta_{self.ciudad}.txt"
        conteo_genero = {}
        
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                genero = datos[1]
                if genero in conteo_genero:
                    conteo_genero[genero] += 1
                else:
                    conteo_genero[genero] = 1

        return conteo_genero
    
encuestas = [
    Encuesta(25, "Masculino", "Bogota", "Buena"),
    Encuesta(30, "Femenino", "Medellin", "Excelente"),
    Encuesta(22, "Masculino", "Cali", "Regular"),
    Encuesta(28, "Femenino", "Bogota", "Mala"),
]

for encuesta in encuestas:
    encuesta.guardar_por_ciudad()
    