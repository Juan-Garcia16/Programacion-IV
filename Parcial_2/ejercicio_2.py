class Habitacion:
    
    def __init__(self, numero, precio, estado="Disponible"):
        self.__numero = numero
        self.__precio = precio
        self.__estado = estado
        
    def get_number(self):
        return self.__numero
        
    def set_number(self, numero):
        self.__numero = numero
            
    def get_price(self):
        return self.__precio
            
    def set_price(self, precio):
        self.__precio = precio
            
    def get_state(self):
        return self.__estado
            
    def set_state(self, estado):
        self.__estado = estado
        
    def reservar(self):
        if self.__estado == "Disponible":
            self.__estado = "Reservada"
            print(f"Habitación {self.__numero} reservada con éxito.")
        else:
            print(f"Habitación {self.__numero} ya está reservada.")
            
    def liberar(self):
        self.__estado = "Disponible"
        print(f"Habitación {self.__numero} ahora está disponible.")
        
    def mostrar_info(self):
        print(f"Número: {self.__numero} | Precio: ${self.__precio} | Estado: {self.__estado}")
            
        
class HabitacionSimple(Habitacion):
    
    def __init__(self, numero, precio):
        super().__init__(numero, precio)
        
    def calcular_precio_total(self):
        return self.get_price
        
    def mostrar_info(self):
        print("Tipo: Habitación Simple")
        super().mostrar_info()
    

class HabitacionDoble(Habitacion): 
    
    def __init__(self, numero, precio):
        super().__init__(numero, precio)
        self.__servicios_adicionales = {} # {"Desayuno": 30.000, "Spa": 50.000 }
        
    def set_servicio(self, servicio, precio):
        self.__servicios_adicionales[servicio] = precio
        
    def calcular_precio_total(self):
        total = self.get_price() + sum(self.__servicios_adicionales.values())
        return total
        
    def mostrar_info(self):
        print("Tipo: Habitación Doble")
        super().mostrar_info()
        if self.__servicios_adicionales:
            print("Servicios adicionales:")
            for nombre, precio in self.__servicios_adicionales.items():
                print(f"  - {nombre}: ${precio}")
            print(f"Precio total: ${self.calcular_precio_total()}")
        else:
            print("Sin servicios adicionales.")
    
    
class HabitacionSuite(Habitacion):
    
    def __init__(self, numero, precio):
        super().__init__(numero, precio)
        self.__servicios_adicionales = {}
        
    def set_servicio(self, servicio, precio):
        self.__servicios_adicionales[servicio] = precio
        
    def calcular_precio_total(self):
        total = self.get_price()+sum(self.__servicios_adicionales.values())
        return total
        
    def mostrar_info(self):
        print("Tipo: Habitación Suite")
        super().mostrar_info()
        if self.__servicios_adicionales:
            print("Servicios adicionales:")
            for nombre, precio in self.__servicios_adicionales.items():
                print(f"  - {nombre}: ${precio}")
            print(f"Precio total: ${self.calcular_precio_total()}")
        else:
            print("Sin servicios adicionales.")
            
class SistemaHotel:
    
    def __init__(self):
        self.__habitaciones = {}  # clave: número habitación, valor: objeto Habitación

    def set_habitacion(self, habitacion):
        self.__habitaciones[habitacion.get_number()] = habitacion
        return self.__habitaciones[habitacion.get_number()]

    def get_disponibles(self):
        print("\n HABITACIONES DISPONIBLES:")
        disponibles = [h for h in self.__habitaciones.values() if h.get_state() == "Disponible"]
        if disponibles:
            for h in disponibles:
                h.mostrar_info()
                print("-" * 40)
        else:
            print("No hay habitaciones disponibles.")

    def reservar_habitacion(self, numero):
        if numero in self.__habitaciones:
            habitacion = self.__habitaciones[numero]
            habitacion.reservar()
        else:
            print("No existe una habitación con ese número.")

    def mostrar_todas(self):
        print("\nTODAS LAS HABITACIONES:")
        for h in self.__habitaciones.values():
            h.mostrar_info()
            print("-" * 40)
            
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
                        elif servicio == "desayuno":
                            habitacion.set_servicio(servicio, 20)
                            print(" Desayuno agregado correctamente.")
                        elif servicio == "spa":
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