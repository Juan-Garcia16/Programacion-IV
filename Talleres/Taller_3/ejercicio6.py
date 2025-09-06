'''
6. Implemente una clase `NotaMusical` con atributos como nombre, frecuencia y
duración. Guarde en un archivo las notas mayores a cierta frecuencia. Añada un
método que simule la ejecución de la nota (texto).
'''

class NotaMusical:
    def __init__(self, nombre, frecuencia, duracion):
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.duracion = duracion
        
    def __str__(self):
        return f"{self.nombre},{self.frecuencia},{self.duracion}"
    
    def guardar_notas_alta_frecuencia(self, nombre_archivo, frecuencia):
        with open(nombre_archivo, "a") as archivo:
            if self.frecuencia > frecuencia:
                archivo.write(str(self) + "\n")
    
    def ejecutar_nota(self):
        print(f"Ejecutando nota {self.nombre} con frecuencia {self.frecuencia} Hz durante {self.duracion} segundos.")
        
notas = [
    NotaMusical("Do", 261.63, 1),
    NotaMusical("Re", 293.66, 1),
    NotaMusical("Mi", 329.63, 3),
    NotaMusical("Fa", 349.23, 1),
    NotaMusical("Sol", 392.00, 4),
    NotaMusical("La", 440.00, 2),
    NotaMusical("Si", 493.88, 1),
]

for nota in notas:
    nota.guardar_notas_alta_frecuencia('notas_altas.txt', 300)
    nota.ejecutar_nota()
    
print("\nNotas con frecuencia mayor a 300 Hz guardadas en 'notas_altas.txt'\n")