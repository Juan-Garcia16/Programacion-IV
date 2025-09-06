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
    
    def estadisticas_por_genero(ciudad):
        nombre_archivo = f"encuesta_{ciudad}.txt"
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
    Encuesta(35, "Masculino", "Medellin", "Buena"),
    Encuesta(40, "Femenino", "Cali", "Excelente"),
    Encuesta(29, "Masculino", "Bogota", "Regular"),
    Encuesta(33, "Femenino", "Medellin", "Mala"),
    Encuesta(26, "Masculino", "Cali", "Buena"),
    Encuesta(31, "Femenino", "Cali", "Excelente")
]

for encuesta in encuestas:
    encuesta.guardar_por_ciudad()

ciudades = []
for encuesta in encuestas:
    if encuesta.ciudad not in ciudades:
        ciudades.append(encuesta.ciudad)

for ciudad in ciudades:
    estadisticas = Encuesta.estadisticas_por_genero(ciudad)
    print(f"\nEstadísticas por género en {ciudad}:")
    for genero, conteo in estadisticas.items():
        print(f"{genero}: {conteo}")