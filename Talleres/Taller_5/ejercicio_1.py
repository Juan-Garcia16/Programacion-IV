'''
a. Para cada clase debe diseñar al menos 6 atributos.
b. Para las clases profesor debe realizar un método en donde se pueda
calcular el sueldo mensual dependiendo de las horas que trabaja y del
tipo de profesor que sea
c. Debe de crear un método para calcular la antigüedad de todas las
entidades en el diseño.
d. Dependiendo de cada tipo de profesor debe diseñar al menos tres
materias acordes con el rango de cada uno y se deben visualizar en
pantalla por medio de un método.
e. Guarde la información que crea necesaria en un archivo para este
programa.
'''
import json

class PersonalUniversitario:
    def __init__(self, codigo, nombre, edad, anio_ingreso, direccion, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.anio_ingreso = anio_ingreso
        self.direccion = direccion
        self.telefono = telefono

    def calcular_antiguedad(self):
        return 2025 - self.anio_ingreso
    
    def informacion_general(self):
        print(f"Nombre: {self.nombre}\nCodigo: {self.codigo}\nEdad: {self.edad}\nDireccion: {self.direccion}\nTelefono: {self.telefono}")
        print(f"Antiguedad: {self.calcular_antiguedad()} años")
    
    def to_dict(self): #para guardar en json
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "edad": self.edad,
            "anio_ingreso": self.anio_ingreso,
            "direccion": self.direccion,
            "telefono": self.telefono
        }
        
class Profesor(PersonalUniversitario):
    def __init__(self, codigo, nombre, edad, anio_ingreso, direccion, telefono,
                 categoria, horas_contrato, tipo_profesor, salario_base, departamento, materias):
        PersonalUniversitario.__init__(self,codigo, nombre, edad, anio_ingreso, direccion, telefono)
        self.categoria = categoria
        self.horas_contrato = horas_contrato
        self.tipo_profesor = tipo_profesor
        self.salario_base = salario_base
        self.departamento = departamento
        self.materias = ["Arquitectura de Computadores", "Ingenieria de Software", "Comunicaciones"] if tipo_profesor.lower() == 'planta' else ["Programacion", "Estructuras de Datos", "Calculo"]
        
    def calcular_sueldo(self):
        if self.tipo_profesor.lower() == 'planta':
            valor_hora = 70000
            horas_pagadas = self.horas_contrato * valor_hora
            salario_total = self.salario_base + horas_pagadas
        elif self.tipo_profesor.lower() == 'ayudante':
            valor_hora = 30000
            horas_pagadas = self.horas_contrato * valor_hora
            salario_total = self.salario_base + horas_pagadas
        else:
            return None
        return salario_total

    def mostrar_materias(self):
        print("Materias asignadas:")
        for materia in self.materias:
            print(f" - {materia}")
            
    def informacion_profesor(self):
        self.informacion_general()
        print(f"| Categoria: {self.categoria} | Tipo Profesor: {self.tipo_profesor} | Departamento: {self.departamento} |")
        self.mostrar_materias()
        print(f"Sueldo: {self.calcular_sueldo()}")
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "categoria": self.categoria,
            "horas_contrato": self.horas_contrato,
            "tipo_profesor": self.tipo_profesor,
            "salario_base": self.salario_base,
            "departamento": self.departamento,
            "materias": self.materias
        })
        return data

class Alumno(PersonalUniversitario):
    def __init__(self, codigo, nombre, edad, anio_ingreso, direccion, telefono,
                 carrera, semestre, promedio, creditos):
        PersonalUniversitario.__init__(self,codigo, nombre, edad, anio_ingreso, direccion, telefono)
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.creditos = creditos
        
    def informacion_alumno(self):
        self.informacion_general()
        print(f"| Carrera: {self.carrera} | Semestre: {self.semestre} | Promedio: {self.promedio} | Creditos: {self.creditos} |")
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "carrera": self.carrera,
            "semestre": self.semestre,
            "promedio": self.promedio,
            "creditos": self.creditos
        })
        return data
        
class ProfesorAyudante(Profesor, Alumno):
    def __init__(self, codigo, nombre, edad, anio_ingreso, direccion, telefono,
                 categoria, horas_contrato, tipo_profesor, salario_base, departamento, materias,
                 carrera, semestre, promedio, creditos):

        Profesor.__init__(self, codigo, nombre, edad, anio_ingreso, direccion, telefono,
                 categoria, horas_contrato, tipo_profesor, salario_base, departamento, materias)

        Alumno.__init__(self, codigo, nombre, edad, anio_ingreso, direccion, telefono,
                        carrera, semestre, promedio, creditos)
        
    def informacion_ayudante(self):
        self.informacion_profesor()
        print(f"| Carrera: {self.carrera} | Semestre: {self.semestre} | Promedio: {self.promedio} | Creditos: {self.creditos} |")
    
    def to_dict(self):
        data = Profesor.to_dict(self)
        data.update(Alumno.to_dict(self))
        return data

def guardar_json(objeto, nombre_archivo):
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        json.dump(objeto.to_dict(), archivo, indent=4, ensure_ascii=False)
        archivo.write("\n")
    print(f"Datos guardados en {nombre_archivo}")
    
#objetos para probar
prof1 = Profesor(
    codigo="P001",
    nombre="Carlos Pérez",
    edad=45,
    anio_ingreso=2010,
    direccion="Calle 45 #12-34",
    telefono="3001112233",
    categoria="Titular",
    horas_contrato=40,
    tipo_profesor="Planta",
    salario_base=2000000,
    departamento="Ingeniería de Sistemas",
    materias=None  #se ignora porque se definen acorde al tipo de profesor
)

prof2 = Profesor(
    codigo="P002",
    nombre="Laura Martínez",
    edad=38,
    anio_ingreso=2015,
    direccion="Carrera 10 #55-20",
    telefono="3012223344",
    categoria="Asociado",
    horas_contrato=20,
    tipo_profesor="Ayudante",
    salario_base=800000,
    departamento="Matemáticas",
    materias=None
)

alum1 = Alumno(
    codigo="A001",
    nombre="Juan Gómez",
    edad=20,
    anio_ingreso=2023,
    direccion="Barrio Centro, Casa 12",
    telefono="3023334455",
    carrera="Ingeniería de Sistemas",
    semestre=3,
    promedio=4.2,
    creditos=48
)

alum2 = Alumno(
    codigo="A002",
    nombre="María Rodríguez",
    edad=21,
    anio_ingreso=2022,
    direccion="Calle 8 #21-50",
    telefono="3034445566",
    carrera="Ingeniería Electrónica",
    semestre=5,
    promedio=3.8,
    creditos=75
)

ayud1 = ProfesorAyudante(
    codigo="PA001",
    nombre="Andrés Torres",
    edad=23,
    anio_ingreso=2021,
    direccion="Carrera 50 #22-10",
    telefono="3045556677",
    categoria="Auxiliar",
    horas_contrato=10,
    tipo_profesor="Ayudante",
    salario_base=500000,
    departamento="Computación",
    materias=None,
    carrera="Ingeniería de Software",
    semestre=7,
    promedio=4.5,
    creditos=90
)

guardar_json(prof1, "profesores.json")
guardar_json(prof2, "profesores.json")
guardar_json(alum1, "alumnos.json")
guardar_json(alum2, "alumnos.json")
guardar_json(ayud1, "ayudantes.json")

print("\n--- PROFESORES ---")
prof1.informacion_profesor()
print()
prof2.informacion_profesor()
print("\n--- ALUMNOS ---")
alum1.informacion_alumno()
print("\n--- PROFESORES AYUDANTES ---")
ayud1.informacion_ayudante()