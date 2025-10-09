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