from sistema import SistemaHotel
from habitaciones import HabitacionSimple, HabitacionDoble, HabitacionSuite
            
def main():
    # Crear sistema
    hotel = SistemaHotel()

    # Crear habitaciones
    h1 = HabitacionSimple(101, 100)
    h2 = HabitacionDoble(202, 180)
    h3 = HabitacionSuite(303, 300)
    
    hotel.set_habitacion(h1)
    hotel.set_habitacion(h2)
    hotel.set_habitacion(h3)
    
    while True:
        print("""===== MENÚ HOTEL =====
        1. Mostrar habitaciones disponibles
        2. Reservar una habitación
        3. Calcular precio total
        4. Agregar servicios a una habitación
        5. Salir""")
                 
        opcion = input("Seleccione una opción: ")
        numero = 0

        if opcion == "1":
            hotel.get_disponibles()
        elif opcion == "2":
            numero = int(input("Ingrese el numero de habitación a reservar: "))
            hotel.reservar_habitacion(numero)
        elif opcion == "3":
            numero = int(input("Ingrese el número de habitación: "))
            if numero in hotel._SistemaHotel__habitaciones:  # acceder al diccionario encapsulado
               habitacion = hotel._SistemaHotel__habitaciones[numero]
               if hasattr(habitacion, "calcular_precio_total"):
                    total = habitacion.calcular_precio_total()
                    print(f"El precio total de la habitación {numero} es: ${total}")
               else:
                    print(f"El precio de la habitación {numero} es: ${habitacion.get_price()}")
            else:
                print("No existe una habitación con ese número.")
        elif opcion == "4":
            numero = int(input("Ingrese el número de habitación: "))
            if numero in hotel._SistemaHotel__habitaciones:  
                habitacion = hotel._SistemaHotel__habitaciones[numero]
        
        
                if isinstance(habitacion, (HabitacionDoble, HabitacionSuite)):
                    while True:
                        print("\nServicios disponibles: Desayuno ($20) | Spa ($50)")
                        servicio = input("Ingrese servicio a agregar (o 'salir' para terminar): ").capitalize()
                
                        if servicio.lower() == "salir":
                            break
                        elif servicio == "Desayuno":
                            habitacion.set_servicio(servicio, 20)
                            print(" Desayuno agregado correctamente.")
                        elif servicio == "Spa":
                            habitacion.set_servicio(servicio, 50)
                            print("Spa agregado correctamente.")
                        else:
                            print("Servicio no válido.")
                else:
                    print("Esta habitación no permite servicios adicionales.")
            else:
                print("No existe una habitación con ese número.")

        elif opcion == "5":
            print("Gracias por usar el sistema de reservas.")
            break
        else:
            print("opción no válida.")


if __name__ == "__main__":
    main()