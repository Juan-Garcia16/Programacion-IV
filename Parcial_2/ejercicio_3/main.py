from sistema_pedidos import Producto, Electronico, Ropa, Alimento, SistemaPedidos

def main():
    sistema = SistemaPedidos()

    sistema.agregar_producto(Electronico("laptop", 350000, 10, 24))
    sistema.agregar_producto(Ropa("camiseta", 50000, 30, "M"))
    sistema.agregar_producto(Alimento("leche", 5000, 20, "10/10/2025"))

    while True:
        print("""\n=== MENÚ TIENDA ONLINE ===
             1. Mostrar productos disponibles
             2. Realizar pedido
             3. Salir""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.mostrar_productos()

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ").lower()
            cantidad = int(input("Ingrese la cantidad: "))
            sistema.realizar_pedido(nombre, cantidad)
            
        elif opcion == "3":
            print("¡Gracias por su compra!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()