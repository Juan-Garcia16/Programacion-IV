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