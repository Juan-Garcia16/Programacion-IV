"""
=====================================================
 RESUMEN DE CONSTRUCTORES ESPECIALES EN PYTHON (POO)
=====================================================

En Python, los constructores especiales (también llamados
métodos mágicos o dunder methods) permiten modificar el 
comportamiento de los objetos en diferentes contextos.
Todos comienzan y terminan con doble guion bajo (__).
"""

# ---------------------------------------------------
# 1. __init__(self, ...)
# ---------------------------------------------------
# Se ejecuta automáticamente al crear una instancia.
# Sirve para inicializar atributos del objeto.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Juan", 20)
print("INIT:", p.nombre, p.edad)


# ---------------------------------------------------
# 2. __new__(cls, ...)
# ---------------------------------------------------
# Se ejecuta antes de __init__.
# Crea la instancia en memoria.
class MiClase:
    def __new__(cls):
        print("NEW: creando instancia")
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self):
        print("INIT: inicializando instancia")

obj = MiClase()


# ---------------------------------------------------
# 3. __str__(self)
# ---------------------------------------------------
# Devuelve una representación amigable en texto 
# cuando se usa print() sobre el objeto.
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"Coche: {self.marca} {self.modelo}"

c = Coche("Toyota", "Corolla")
print("STR:", c)


# ---------------------------------------------------
# 4. __repr__(self)
# ---------------------------------------------------
# Devuelve una representación oficial y útil 
# para desarrolladores (depuración).
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"

p = Punto(2, 3)
print("REPR:", p)


# ---------------------------------------------------
# 5. __del__(self)
# ---------------------------------------------------
# Se ejecuta cuando el objeto va a ser eliminado 
# por el recolector de basura.
class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Recurso {self.nombre} creado")

    def __del__(self):
        print(f"Recurso {self.nombre} liberado")

r = Recurso("Archivo")
del r  # Fuerza la destrucción


# ---------------------------------------------------
# 6. __call__(self, ...)
# ---------------------------------------------------
# Permite llamar al objeto como si fuera una función.
class Funcional:
    def __init__(self, valor):
        self.valor = valor
    
    def __call__(self, incremento):
        self.valor += incremento
        return self.valor

f = Funcional(10)
print("CALL:", f(5))  # f actúa como función


# ---------------------------------------------------
# 7. __len__(self)
# ---------------------------------------------------
# Define el comportamiento de len(obj).
class Coleccion:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def __len__(self):
        return len(self.elementos)

col = Coleccion([1, 2, 3, 4])
print("LEN:", len(col))


# ---------------------------------------------------
# 8. __getitem__(self, key)
# ---------------------------------------------------
# Permite acceder a elementos usando corchetes obj[key].
class Diccionario:
    def __init__(self):
        self.datos = {"a": 1, "b": 2}
    
    def __getitem__(self, clave):
        return self.datos.get(clave, "No encontrado")

d = Diccionario()
print("GETITEM:", d["a"], d["c"])

"""
=====================================================
 FIN DEL RESUMEN
=====================================================
"""
