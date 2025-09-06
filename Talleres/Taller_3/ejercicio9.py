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
    
    def guardar_reporte_por_departamento(empleados, nombre_archivo):
        departamentos = {}
        for empleado in empleados:
            if empleado.departamento not in departamentos:
                #crear una lista para el nuevo departamento
                departamentos[empleado.departamento] = []
            departamentos[empleado.departamento].append(empleado)
        
        with open(nombre_archivo, "w") as archivo:
            for departamento, empleado_lista in departamentos.items():
                archivo.write(f"Departamento: {departamento}\n")
                for empleado in empleado_lista:
                    archivo.write(str(empleado) + "\n")
                archivo.write("\n")
        print(f"Reporte guardado en '{nombre_archivo}'\n")