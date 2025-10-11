class Empleado():
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario):
        self.__nombre = nombre
        self.__id_empleado = id_empleado
        self.__correo = correo
        self.__telefono = telefono
        self.__tipo_empleado = tipo_empleado
        self.__salario =  salario
        
    def get_nombre(self):
        return self.__nombre
    def get_id_empleado(self):
        return self.__id_empleado
    def get_correo(self):
        return self.__correo
    def get_telefono(self):
        return self.__telefono
    def get_tipo_empleado(self):
        return self.__tipo_empleado
    def get_salario(self):
        return self.__salario
    
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")
    def set_id_empleado(self, nuevo_id):
        if isinstance(nuevo_id, int) and nuevo_id > 0:
            self.__id_empleado = nuevo_id
        else:
            raise ValueError("El ID del empleado debe ser un número positivo")
    def set_correo(self, nuevo_correo):
        if isinstance(nuevo_correo, str) and "@" in nuevo_correo:
            self.__correo = nuevo_correo
        else:
            raise ValueError("El correo debe ser una cadena de texto válida")
    def set_telefono(self, nuevo_telefono):
        if isinstance(nuevo_telefono, str) and nuevo_telefono.isdigit():
            self.__telefono = nuevo_telefono
        else:
            raise ValueError("El teléfono debe ser una cadena de dígitos")
    def set_tipo_empleado(self, nuevo_tipo):
        if isinstance(nuevo_tipo, str):
            self.__tipo_empleado = nuevo_tipo
        else:
            raise ValueError("El tipo de empleado debe ser una cadena de texto")
    def set_salario(self, nuevo_salario):
        if isinstance(nuevo_salario, (int, float)) and nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            raise ValueError("El salario debe ser un número positivo")
        
        
        
    def informacion_empleado(self):
        print(f"Nombre: {self.__nombre}\nID: {self.__id_empleado}\nCorreo: {self.__correo}\nTelefono: {self.__telefono}\nSalario: {self.__salario}")

    def calcular_bono(self, porcentaje):
        bono = self.__salario * (porcentaje / 100)
        return bono
    
    def mostrar_informacion(self):
        print(f"Empleado: {self.__nombre}, ID: {self.__id_empleado}, Tipo: {self.__tipo_empleado}, Salario: {self.__salario}")

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "id_empleado": self.__id_empleado,
            "correo": self.__correo,
            "telefono": self.__telefono,
            "tipo_empleado": self.__tipo_empleado,
            "salario": self.__salario
        }
        
class Proyecto():
    def __init__(self, nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado):
        self.__nombre_proyecto = nombre_proyecto
        self.__codigo = codigo
        self.__cliente = cliente
        self.__presupuesto = presupuesto
        self.__duracion_meses = duracion_meses
        self.__equipo_asignado = equipo_asignado
        
    def get_nombre_proyecto(self):
        return self.__nombre_proyecto  
    def get_codigo(self):
        return self.__codigo
    def get_cliente(self):
        return self.__cliente
    def get_presupuesto(self):
        return self.__presupuesto
    def get_duracion_meses(self):
        return self.__duracion_meses
    def get_equipo_asignado(self):  
        return self.__equipo_asignado
    
    def set_nombre_proyecto(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self.__nombre_proyecto = nuevo_nombre
        else:
            raise ValueError("El nombre del proyecto debe ser una cadena de texto")
    def set_codigo(self, nuevo_codigo):
        if isinstance(nuevo_codigo, str):
            self.__codigo = nuevo_codigo
        else:
            raise ValueError("El código del proyecto debe ser una cadena de texto")
    def set_cliente(self, nuevo_cliente):
        if isinstance(nuevo_cliente, str):
            self.__cliente = nuevo_cliente
        else:
            raise ValueError("El cliente debe ser una cadena de texto")
    def set_presupuesto(self, nuevo_presupuesto):
        if isinstance(nuevo_presupuesto, (int, float)) and nuevo_presupuesto > 0:
            self.__presupuesto = nuevo_presupuesto
        else:
            raise ValueError("El presupuesto debe ser un número positivo")
    def set_duracion_meses(self, nueva_duracion):
        if isinstance(nueva_duracion, int) and nueva_duracion > 0:
            self.__duracion_meses = nueva_duracion
        else:
            raise ValueError("La duración en meses debe ser un número entero positivo")
    def set_equipo_asignado(self, nuevo_equipo):
        if isinstance(nuevo_equipo, list):
            self.__equipo_asignado = nuevo_equipo
        else:
            raise ValueError("El equipo asignado debe ser una lista de nombres")
        
        
    def costo_mensual(self):
        return self.__presupuesto / self.__duracion_meses

    def mostrar_proyecto(self):
        print(f"Proyecto: {self.__nombre_proyecto}, Codigo: {self.__codigo}, Cliente: {self.__cliente}, Presupuesto: {self.__presupuesto}, Duracion: {self.__duracion_meses} meses")

    def to_dict(self):
        return {
            "nombre_proyecto": self.__nombre_proyecto,
            "codigo": self.__codigo,
            "cliente": self.__cliente,
            "presupuesto": self.__presupuesto,
            "duracion_meses": self.__duracion_meses,
            "equipo_asignado": self.__equipo_asignado
        }
    
class Junior(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 lenguaje_principal, mentor, framework):
        super().__init__(nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        self.__lenguaje_principal = lenguaje_principal
        self.__mentor = mentor
        self.__framework = framework

    def mostrar_stack(self):
        print(f"Lenguaje Principal: {self.__lenguaje_principal}, Mentor: {self.__mentor}, Framework: {self.__framework}")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "lenguaje_principal": self.__lenguaje_principal,
            "mentor": self.__mentor,
            "framework": self.__framework
        })
        return data
    
class Senior(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 anios_experiencia, especialidad):
        super().__init__(nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        self.__anios_experiencia = anios_experiencia
        self.__especialidad = especialidad

    def calcular_salario_total(self):
        bonus = 0.05 * self.get_salario() * self.__anios_experiencia
        return self.get_salario() + bonus

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "anios_experiencia": self.__anios_experiencia,
            "especialidad": self.__especialidad
        })
        return data
    
class Tester(Empleado):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 herramientas, tipo_prueba):
        super().__init__(nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        self.__herramientas = herramientas
        self.__tipo_prueba = tipo_prueba

    def ejecutar_prueba(self):
        print(f"{self.get_nombre()} ejecuta prueba tipo {self.__tipo_prueba} con {self.__herramientas}")

class ProjectManager(Empleado, Proyecto):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario,
                 nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado,
                 metodologia, reportes):
        Empleado.__init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario)
        Proyecto.__init__(self, nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado)
        self.__metodologia = metodologia
        self.__reportes = reportes

    def generar_reporte(self, descripcion):
        self.__reportes.append(descripcion)
        print(f"Reporte añadido: {descripcion}")

class LiderTecnico(Senior, Proyecto):
    def __init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario, anios_experiencia, especialidad,
                 nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado,
                 certificaciones, tecnologias):
        Senior.__init__(self, nombre, id_empleado, correo, telefono, tipo_empleado, salario, 
                        anios_experiencia, especialidad)
        Proyecto.__init__(self, nombre_proyecto, codigo, cliente, presupuesto, duracion_meses, equipo_asignado)
        self.__certificaciones = certificaciones
        self.__tecnologias = tecnologias

    def listar_tecnologias(self):
        print(f"Tecnologias implementadas por {self.get_nombre()}: {', '.join(self.__tecnologias)}")