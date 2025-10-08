from libros import Libro

def main():
    direccion_archivo = "libros.json"
    libro = Libro()

    while True:
        print("\n===== GESTOR DE LIBROS =====")
        print("1. Agregar libros")
        print("2. Ver libros guardados")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro.guardar_libros(direccion_archivo)
        elif opcion == "2":
            libro.cargar_libros(direccion_archivo)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()