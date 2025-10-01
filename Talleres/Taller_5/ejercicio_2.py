'''2. Diseñe y modele un problema de cotidianidad con herencia múltiple,
implementando las siguientes características:
a. Debe tener al menos dos clases principales.
b. Debe tener al menos 5 subclases.
c. Las clases principales deben tener cada una al menos 5 atributos.
d. Entre todas las clases principales y subclases deben diseñar al menos 7
métodos.
e. Se debe crear una lista para almacenar los objetos creados para probar
las clases y subclases.
f. Guarde la información que crea necesaria en un archivo para este
programa.
'''
class Empleado():
    def __init__(self, nombre, id_empleado, correo, telefono, salario):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.correo = correo
        self.telefono = telefono
        self.salario = salario

class Proyecto():
    def __init__(self, nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado):
        self.nombre_proyecto = nombre_proyecto
        self.codigo = codigo
        self.cliente = cliente
        self.presupuesto = presupuesto
        self.duracion_meses = duracion_meses
        self.equipo_asignado = equipo_asignado
    
class Junior(Empleado):
    def __init__(self, codigo, nombre, id_empleado, correo, telefono, anio_ingreso,
                 lenguaje_principal, mentor, framework):
        super().__init__(codigo, nombre, id_empleado, correo, telefono, anio_ingreso)
        self.lenguaje_principal = lenguaje_principal
        self.mentor = mentor
        self.framework = framework
    
class Senior(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, salario,
                 anios_experiencia, especialidad):
        super().__init__(nombre, id_empleado, correo, telefono, salario)
        self.anios_experiencia = anios_experiencia
        self.especialidad = especialidad
    
class Tester(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, salario,
                 herramientas, tipo_prueba):
        super().__init__(nombre, id_empleado, correo, telefono, salario)
        self.herramientas = herramientas
        self.tipo_prueba = tipo_prueba
    
class ProjectManager(Empleado, Proyecto):
    def __init__(self, nombre, id_empleado, correo, telefono, salario):
        super().__init__(nombre, id_empleado, correo, telefono, salario)
    
class LiderTecnico(Senior, Proyecto):
    hola = 5