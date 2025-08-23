'''
4. Registro de clientes
- Crea una clase `Cliente` con al menos 5 atributos (id, nombre, edad, ciudad, saldo).
- Implemente un método que guarde los clientes en `clientes.txt`.
- Otro método que lea el archivo y muestre solo los clientes con saldo negativo.
'''

class Cliente:
    def __init__(self, id, nombre, edad, ciudad, saldo):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        self.saldo = saldo

    def guardar_clientes(clientes, archivo_clientes = "clientes.txt"):
        for cliente in clientes:
            archivo = open(archivo_clientes, "w")
            # archivo.write(cliente + "\n")
            print(str(cliente))
        #archivo.close()
        
        
clientes = [
    Cliente(1, "Juan Pérez", 30, "Bogotá", 5000),
    Cliente(2, "Ana Gómez", 25, "Medellín", -2000),
    Cliente(3, "Luis Torres", 40, "Cali", 10000),
    Cliente(4, "María López", 35, "Barranquilla", -1500),
    Cliente(5, "Pedro Ruiz", 28, "Cartagena", 0),
]

Cliente.guardar_clientes(clientes)
