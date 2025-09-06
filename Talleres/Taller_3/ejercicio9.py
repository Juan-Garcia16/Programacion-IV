'''
9. Diseñe una clase `Empresa` que maneje empleados, sus salarios, bonificaciones y
descuentos. Incluya métodos para generar reportes en archivos separados por
departamentos.
'''
class Empresa:
    def __init__(self, nombre, departamento, salario, bonificacion, descuento):
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
        self.bonificacion = bonificacion
        self.descuento = descuento
        
    #va primero para incluirlo en el str
    def salario_neto(self):
        return self.salario + self.bonificacion - self.descuento
    
    def __str__(self):
        return f"{self.nombre},{self.departamento},{self.salario},{self.bonificacion},{self.descuento},{self.salario_neto()}"
    
    def guardar_reporte_por_departamento(empleados):
        departamentos = {}
        for empleado in empleados:
            if empleado.departamento not in departamentos:
                departamentos[empleado.departamento] = []
            departamentos[empleado.departamento].append(empleado)

        for departamento, lista_empleados in departamentos.items():
            nombre_archivo = f"reporte_{departamento}.txt"
            with open(nombre_archivo, "w") as archivo:
                for emp in lista_empleados:
                    archivo.write(str(emp) + "\n")
            print(f"Reporte guardado en '{nombre_archivo}'")
        
        
empleados = [
    Empresa("Juan Perez", "Ventas", 3000, 500, 200),
    Empresa("Ana Gomez", "Marketing", 3500, 600, 300),
    Empresa("Luis Martinez", "Ventas", 3200, 400, 150),
    Empresa("Maria Lopez", "Recursos Humanos", 4000, 700, 250),
    Empresa("Carlos Sanchez", "Marketing", 3600, 500, 200),
    Empresa("Sofia Ramirez", "Recursos Humanos", 4200, 800, 300),
    Empresa("Pedro Torres", "Ventas", 3100, 450, 180),
    Empresa("Laura Martinez", "Ventas", 3700, 550, 220),
]

Empresa.guardar_reporte_por_departamento(empleados)
