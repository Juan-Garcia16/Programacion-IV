'''
3. Crea un sistema de gestión de pedidos para una tienda en línea. Los productos pueden ser
de diferentes tipos (Electrónico, Ropa, Alimento). Cada producto tiene un nombre, precio
y cantidad disponible. Los productos electrónicos tienen un período de garantía, la ropa
tiene un tamaño y los alimentos tienen una fecha de caducidad. El sistema debe gestionar
el stock, permitir realizar pedidos y calcular el total de la compra con un posible descuento
si se compra una cierta cantidad de productos.
Requerimientos:
a. Crear una clase base Producto con atributos nombre, precio y cantidad.

b. Crear subclases Electrónico, Ropa y Alimento, cada una con su atributo específico.

c. Crear un sistema de gestión de pedidos que permita:

d. Mostrar los productos disponibles.

e. Realizar un pedido, actualizando la cantidad disponible.

f. Calcular el total de la compra, aplicando un descuento si el cliente compra más de
   5 unidades de un mismo producto.

g. Guardar los productos en un archivo JSON.
'''

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
        
    def set_precio(self, precio):
        self.__precio = precio
        
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_info(self):
        return f"{self.__nombre} - ${self.__precio} - Cantidad: {self.__cantidad}"
        
class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.__garantia = garantia
        
    def get_garantia(self):
        return self.__garantia

    def set_garantia(self, garantia):
        self.__garantia = garantia

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Garantía: {self.__garantia} meses"


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.__talla = talla

    def get_talla(self):
        return self.__talla

    def set_talla(self, talla):
        self.__talla = talla
        
    def mostrar_info(self):
        return f"{super().mostrar_info()} - Talla: {self.__talla}"


class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, caducidad):
        super().__init__(nombre, precio, cantidad)
        self.__caducidad = caducidad
        
    def get_caducidad(self):
        return self.__caducidad

    def set_caducidad(self, caducidad):
        self.__caducidad = caducidad

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Vence: {self.__caducidad}"


class SistemaPedidos:
    def __init__(self):
        self.__productos = {}  # clave -> nombre del producto, valor -> objeto Producto

    def agregar_producto(self, producto):
        self.__productos[producto.get_nombre()] = producto

    def mostrar_productos(self):
        if not self.__productos:
            print("No hay productos disponibles.")
        else:
            print("\n=== PRODUCTOS DISPONIBLES ===")
            for p in self.__productos.values():
                print(p.mostrar_info())
                
    def realizar_pedido(self, nombre, cantidad):
        if nombre in self.__productos:
            producto = self.__productos[nombre]
            if producto.get_cantidad() >= cantidad:
                total = producto.get_precio() * cantidad
                producto.set_cantidad(producto.get_cantidad() - cantidad)
                print(f"Pedido realizado: {cantidad} x {producto.get_nombre()}")
                print(f"Total a pagar: ${total:.2f}")
            else:
                print("Stock insuficiente.")
        else:
            print("Producto no encontrado.")

def main():
    sistema = SistemaPedidos()

    sistema.agregar_producto(Electronico("Laptop", 350000, 10, 24))
    sistema.agregar_producto(Ropa("Camiseta", 50000, 30, "M"))
    sistema.agregar_producto(Alimento("Leche", 5000, 20, "10/10/2025"))

    while True:
        print("""=== MENÚ TIENDA ONLINE ===
             1. Mostrar productos disponibles
             2. Realizar pedido
             3. Salir""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.mostrar_productos()

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            sistema.realizar_pedido(nombre, cantidad)
            
        elif opcion == "3":
            print("¡Gracias por su compra!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()