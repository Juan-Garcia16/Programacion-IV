'''
2. Diseñe una clase `Estudiante` con atributos como nombre, código, carrera, edad y
promedio. Implemente métodos para calcular si el estudiante aprueba (promedio >=
3.0), y guardar los datos en un archivo.
'''
class Estudiante:
    def __init__(self, nombre, codigo, carrera, edad, promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio
        
    def __str__(self):
        return f"{self.nombre},{self.codigo},{self.carrera},{self.edad},{self.promedio}"
    
    def aprobado(self, nombre_archivo):
        estado = "APROBADO" if self.promedio >= 3.0 else "NO APROBADO"
        with open(nombre_archivo, "a") as archivo:
            archivo.write(str(self) + "," + estado + "\n")
        return estado
                
estudiantes = [
    Estudiante("Juan Pérez", "20231001", "Ingeniería de Sistemas", 20, 3.5),
    Estudiante("María López", "20231002", "Medicina", 22, 4.2),
    Estudiante("Carlos Gómez", "20231003", "Derecho", 19, 2.8),
    Estudiante("Ana Torres", "20231004", "Arquitectura", 21, 3.0),
    Estudiante("Pedro Ramírez", "20231005", "Economía", 23, 2.5),
    Estudiante("Laura Sánchez", "20231006", "Psicología", 20, 3.9),
    Estudiante("Luis Fernández", "20231007", "Ingeniería Civil", 24, 2.7),
    Estudiante("Sofía Martínez", "20231008", "Contaduría", 22, 3.3),
    Estudiante("Andrés Rojas", "20231009", "Administración de Empresas", 21, 3.8),
    Estudiante("Camila Herrera", "20231010", "Ingeniería Electrónica", 19, 2.9)
]
        
        
for estudiante in estudiantes:
    estado = estudiante.aprobado('estudiantes.txt')
    print(f"Estudiante: {estudiante.nombre}, Estado: {estado}")

print("Estado de estudiantes guardado en 'estudiantes.txt'")

        