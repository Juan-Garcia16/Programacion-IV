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
import json

class Empleado():
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.correo = correo
        self.telefono = telefono
        self.tipo_empleado = tipo_empleado
        self.salario =  salario
    def informacion_empleado(self):
        print(f"Nombre: {self.nombre}\nID: {self.id_empleado}\nCorreo: {self.correo}\nTelefono: {self.telefono}\nSalario: {self.salario}")

    def calcular_bono(self, porcentaje):
        bono = self.salario * (porcentaje / 100)
        return bono
    
    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, ID: {self.id_empleado}, Tipo: {self.tipo_empleado}, Salario: {self.salario}")
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_empleado": self.id_empleado,
            "correo": self.correo,
            "telefono": self.telefono,
            "tipo_empleado": self.tipo_empleado,
            "salario": self.salario
        }
        
class Proyecto():
    def __init__(self, nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado):
        self.nombre_proyecto = nombre_proyecto
        self.codigo = codigo
        self.cliente = cliente
        self.presupuesto = presupuesto
        self.duracion_meses = duracion_meses
        self.equipo_asignado = equipo_asignado
        
    def costo_mensual(self):
        return self.presupuesto / self.duracion_meses
    
    def mostrar_proyecto(self):
        print(f"Proyecto: {self.nombre_proyecto}, Codigo: {self.codigo}, Cliente: {self.cliente}, Presupuesto: {self.presupuesto}, Duracion: {self.duracion_meses} meses")
        
    def to_dict(self):
        return {
            "nombre_proyecto": self.nombre_proyecto,
            "codigo": self.codigo,
            "cliente": self.cliente,
            "presupuesto": self.presupuesto,
            "duracion_meses": self.duracion_meses,
            "equipo_asignado": self.equipo_asignado
        }
    
class Junior(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 lenguaje_principal, mentor, framework):
        super().__init__(nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        self.lenguaje_principal = lenguaje_principal
        self.mentor = mentor
        self.framework = framework
        
    def mostrar_stack(self):
        print(f"Lenguaje Principal: {self.lenguaje_principal}, Mentor: {self.mentor}, Framework: {self.framework}")
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "lenguaje_principal": self.lenguaje_principal,
            "mentor": self.mentor,
            "framework": self.framework
        })
        return data
    
class Senior(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 anios_experiencia, especialidad):
        super().__init__(nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        self.anios_experiencia = anios_experiencia
        self.especialidad = especialidad
        
    def calcular_salario_total(self):
        bonus = 0.05 * self.salario * self.anios_experiencia
        return self.salario + bonus
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "anios_experiencia": self.anios_experiencia,
            "especialidad": self.especialidad
        })
        return data
    
class Tester(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 herramientas, tipo_prueba):
        super().__init__(nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        self.herramientas = herramientas
        self.tipo_prueba = tipo_prueba
        
    def ejecutar_prueba(self):
        print(f"{self.nombre} ejecuta prueba tipo {self.tipo_prueba} con {self.herramientas}")
    
class ProjectManager(Empleado, Proyecto):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado,
                 metodologia, reportes):
        Empleado.__init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        Proyecto.__init__(self, nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado)
        self.metodologia = metodologia
        self.reportes = reportes
        
    def generar_reporte(self, descripcion):
        self.reportes.append(descripcion)
        print(f"Reporte añadido: {descripcion}")

class LiderTecnico(Senior, Proyecto):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario, anios_experiencia, especialidad,
                 nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado,
                 certificaciones, tecnologias):
        Senior.__init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario, 
                        anios_experiencia, especialidad)
        Proyecto.__init__(self, nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado)
        self.certificaciones = certificaciones
        self.tecnologias = tecnologias
        
    def listar_tecnologias(self):
        print(f"Tecnologias implementadas por {self.nombre}: {', '.join(self.tecnologias)}")
        

empleados = []
proyectos = []

j1 = Junior("Ana", 101, "ana@mail.com", "3001234567", "Junior", 3000,
            "Python", "Carlos", "Django")
s1 = Senior("Luis", 102, "luis@mail.com", "3007654321", "Senior", 8000,
            5, "Backend")
t1 = Tester("Marta", 103, "marta@mail.com", "3009998887", "Tester", 4000,
            ["Selenium"], "Automatizada")

p1 = Proyecto("Sistema de Inventario", "P001", "ClienteX", 50000, 10, ["Ana", "Luis", "Marta"])

pm1 = ProjectManager("Laura", 104, "laura@mail.com", "3011239876", "Project Manager", 12000,
                     "Sistema de Inventario", "P001", "ClienteX", 50000, 10, ["Ana", "Luis", "Marta"],
                     "Scrum", []) #no se me ocurren reportes, pero seria un campo de descripcion

lt1 = LiderTecnico("Pedro", 105, "pedro@mail.com", "3027654321", "Lider Tecnico", 10000, 8, "Arquitectura",
                   "Sistema de Inventario", "P001", "ClienteX", 50000, 10, ["Ana", "Luis", "Marta"],
                   ["AWS", "Docker"], ["Python", "Kubernetes"])

empleados.extend([j1, s1, t1, pm1, lt1])
proyectos.append(p1)

print("\n--- INFORMACION EMPLEADOS ---")
for e in empleados:
    e.mostrar_informacion()

print("\n--- STACK JUNIORS ---")
j1.mostrar_stack()

print("\n--- SALARIO SENIORS ---")
print(f"Salario total de {s1.nombre}: {s1.calcular_salario_total()}")

print("\n--- DIAGNOSTICO TESTER ---")
t1.ejecutar_prueba()

print("\n--- INFORMACION PROYECTO ---")
p1.mostrar_proyecto()
print(f"Costo mensual: {p1.costo_mensual()}")

print("\n--- REPORTE PROJECT MANAGER ---")
pm1.generar_reporte("Sprint 1 completado exitosamente")

print("\n--- TECNOLOGIAS DEL LIDER TECNICO ---")
lt1.listar_tecnologias()


def guardar_lista_json(lista_objetos, nombre_archivo):
    datos = [obj.to_dict() for obj in lista_objetos]
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

guardar_lista_json(empleados, "empleados.json")
guardar_lista_json(proyectos, "proyectos.json")
print("\n\nDatos guardados en empleados.json y proyectos.json")
