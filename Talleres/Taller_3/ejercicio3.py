'''
3. Cree una clase `InventarioProducto` que gestione un listado de productos (nombre,
precio, cantidad). Agregue métodos para añadir productos, calcular el valor total del
inventario y guardar todo en un archivo.
'''

class InventarioProducto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def __str__(self):
        return f"{self.nombre},{self.precio},{self.cantidad}"

    def agregar_productos(self, lista_productos):
        lista_productos.append(self)
        return lista_productos
    
    def total_inventario(lista_productos):
        total = 0
        for producto in lista_productos:
            total += (producto.precio) * (producto.cantidad)
        return total

    def guardar_archivo(lista_productos, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            for producto in lista_productos:
                archivo.write(str(producto) + "\n")
        print(f"Se guardó el inventario en '{nombre_archivo}'\n")

productos = []

while True:
    opcion = int(input("Seleccione una opción:\n1. Agregar producto\n2. Calcular valor total del inventario\n3. Guardar inventario en archivo\n4. Salir\n"))
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        producto = InventarioProducto(nombre, precio, cantidad)
        productos = producto.agregar_productos(productos)
    elif opcion == 2:
        total = InventarioProducto.total_inventario(productos)
        print(f"El valor total del inventario es: {total}\n")
    elif opcion == 3:
        InventarioProducto.guardar_archivo(productos, "inventario.txt")
    elif opcion == 4:
        break
    else:
        print("Opción no valida. Intente nuevamente\n")
