'''
10. Desarrolle una clase `SistemaNotas` para manejar múltiples estudiantes y sus
calificaciones. Implemente métodos para calcular promedios por materia y guardar los
mejores estudiantes en un archivo.
'''

#fue la forma menos complicada que encontre de hacerlo, por eso esta clase
class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas #lista de notas
    
    def promedio(self):
        return sum(self.notas) / len(self.notas)
    
    def __str__(self):
        return f"{self.nombre}: {self.notas} -> Promedio: {self.promedio():.2f}"


class SistemaNotas:
    def __init__(self, materias):
        self.materias = materias
        self.estudiantes = []# Lista de objetos Estudiante
    
    def agregar_estudiante(self, nombre, notas):
        self.estudiantes.append(Estudiante(nombre, notas))
    
    def promedio_por_materia(self):
        promedios = []
        num_materias = len(self.materias)
        
        for i in range(num_materias):
            suma = 0
            for estudiante in self.estudiantes:
                suma += estudiante.notas[i]
            promedios.append(round(suma / len(self.estudiantes), 2))
        
        #se crea un diccionario con las materias y sus promedios
        return {self.materias[i]: promedios[i] for i in range(num_materias)}
    
    def guardar_mejores_estudiantes(self, archivo, n=3):
        ordenados = sorted(self.estudiantes, key=Estudiante.promedio, reverse=True)
        
        with open(archivo, "w") as f:
            for estudiante in ordenados[:n]:
                f.write(f"{estudiante.nombre},{estudiante.promedio():.2f}\n")
        
        print(f"Archivo '{archivo}' generado con los {n} mejores estudiantes")


sistema = SistemaNotas(["Matemáticas", "Física", "Programación"])

sistema.agregar_estudiante("Juan", [4.5, 3.8, 4.9])
sistema.agregar_estudiante("María", [4.8, 4.2, 4.7])
sistema.agregar_estudiante("Luis", [3.9, 4.5, 4.3])
sistema.agregar_estudiante("Ana", [4.7, 4.9, 5.0])

print("\nPromedios por materia:", sistema.promedio_por_materia())
sistema.guardar_mejores_estudiantes("mejores_estudiantes.txt", n=3)
