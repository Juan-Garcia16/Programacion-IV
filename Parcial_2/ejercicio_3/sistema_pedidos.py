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
from generador import generar_json ,leer_json

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
    
    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "precio": self.__precio,
            "cantidad": self.__cantidad
        }
        
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
    
    def to_dict(self):
        data = super().to_dict()
        data["garantia"] = self.__garantia
        return data


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
    
    def to_dict(self):
        data = super().to_dict()
        data["talla"] = self.__talla
        return data


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
    
    def to_dict(self):
        data = super().to_dict()
        data["caducidad"] = self.__caducidad
        return data


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
                descuento = 0
                if cantidad > 5:
                    descuento = total * 10/100  #aplicar descuento del 10%
                    print(f"Se aplicó un descuento de ${descuento:.2f} por comprar más de 5 unidades.")
                print(f"Pedido realizado: {cantidad} x {producto.get_nombre()}")
                print(f"Total a pagar: ${total - descuento:.2f}")
                
                self.guardar_productos()  # Actualizar el archivo JSON después de cada pedido
            else:
                print("Stock insuficiente.")
        else:
            print("Producto no encontrado.")
            
    def guardar_productos(self, archivo="productos.json"):
        datos = []
        for p in self.__productos.values():
            datos.append(p.to_dict())
            
        generar_json(archivo, datos)
        print(f"stock actualizado en {archivo}")

    # Cargar productos desde el archivo JSON
    def cargar_productos(self, direccion_archivo):
        productos = leer_json(direccion_archivo)
        if productos:
            print("\n---Lista de productos guardados---")
            for producto in productos:
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, "
                      f"Cantidad: {producto['cantidad']}, Tipo: {producto['tipo']}")
        else:
            print("No se pudieron cargar los productos o el archivo está vacío.")

