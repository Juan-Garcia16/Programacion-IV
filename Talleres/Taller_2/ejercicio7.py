'''
7. Inventario de almacén
- Crea una clase `Producto` con atributos: código, nombre, cantidad, precio y
categoría.
- Implemente un método que permita guardar el inventario en `almacen.txt`.
- Otro método que lea el archivo y muestre el valor total en stock de cada categoría.
'''
class Producto:
    def __init__(self, codigo, nombre, cantidad, precio, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
    
    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio},{self.categoria}"
    
    def guardar_inventario(productos, archivo = "almacen.txt"):
        archivo = open(archivo, "w")
        for producto in productos:
            archivo.write(str(producto) + "\n")
        archivo.close()
        
    def total_stock_categorias(archivo = "almacen.txt"):
        stock_por_categoria = {}
        archivo = open(archivo, "r")
        
        for linea in archivo:
            datos = linea.strip().split(",")
            cantidad = int(datos[2])
            precio = float(datos[3])
            categoria = datos[4]
            stock = cantidad * precio

            if categoria in stock_por_categoria:
                stock_por_categoria[categoria] += stock
            else:
                stock_por_categoria[categoria] = stock
        archivo.close()
        
        print("\nStock total por categoria:")
        for categoria, total in stock_por_categoria.items():
            print(f"{categoria}: {total}")

productos = [
    Producto("001", "Laptop", 10, 3500.00, "Electrónica"),
    Producto("010", "Zapatos deportivos", 18, 150.00, "Calzado"),
    Producto("002", "Mouse", 50, 25.00, "Electrónica"),
    Producto("003", "Teclado", 30, 45.00, "Electrónica"),
    Producto("004", "Silla ergonómica", 15, 750.00, "Muebles"),
    Producto("005", "Escritorio", 12, 1200.00, "Muebles"),
    Producto("007", "Leche", 80, 3.50, "Alimentos"),
    Producto("008", "Camisa", 25, 60.00, "Ropa"),
    Producto("009", "Pantalón", 20, 90.00, "Ropa"),
    Producto("006", "Café molido", 100, 15.00, "Alimentos"),
]

Producto.guardar_inventario(productos)
Producto.total_stock_categorias()