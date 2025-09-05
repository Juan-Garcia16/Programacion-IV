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
        
    def __str__(self): #define como se convierte a cadena el objeto
        return f"{self.id},{self.nombre},{self.edad},{self.ciudad},{self.saldo}"

    def guardar_clientes(clientes, archivo_clientes = "clientes.txt"):
        archivo = open(archivo_clientes, "w")
        for cliente in clientes:
            archivo.write(str(cliente) + "\n")
        archivo.close()
        
    def leer_clientes(archivo_clientes = "clientes.txt"):
        archivo = open(archivo_clientes, "r")
        encontrados = False
        print("Clientes con saldos negativos:")
        for linea in archivo:
            datos = linea.strip().split(",")
            saldo = float(datos[4])
            if saldo < 0:
                print(f"Id: {datos[0]}, Nombre: {datos[1]}, Edad: {datos[2]}, Ciudad: {datos[3]}, Sueldo: {datos[4]}")
                encontrados = True
        if not encontrados:
            print("No hay clientes con saldos negativos")
        
        archivo.close()
        
             
clientes = [
    Cliente(1, "Juan Pérez", 30, "Bogotá", 5000),
    Cliente(2, "Ana Gómez", 25, "Medellín", -2000),
    Cliente(3, "Luis Torres", 40, "Cali", 10000),
    Cliente(4, "María López", 35, "Barranquilla", -1500),
    Cliente(5, "Pedro Ruiz", 28, "Cartagena", 0),
]

Cliente.guardar_clientes(clientes)
Cliente.leer_clientes()
