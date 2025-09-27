'''
4. Crea una clase base Transporte con atributos capacidad y tarifa.
Subclases: Bus, Taxi y Metro, cada una sobrescribe un método
calcular_pasaje(km) que determine el costo según la distancia recorrida.
Ejemplo:
Bus: tarifa fija + (100 * km)
Taxi: (500 * km)
Metro: tarifa fija sin importar los km
Crea varios transportes y muestra el costo de un trayecto de 10 km para cada uno
usando polimorfismo.
'''
class Transporte:
    def __init__(self, capacidad, tarifa_fija=0):
        self.capacidad = capacidad
        self.tarifa_fija = tarifa_fija

    def calcular_pasaje(self, km):
        pass

class Bus(Transporte):
    def calcular_pasaje(self, km):
        return self.tarifa_fija + (100 * km)

class Taxi(Transporte):
    def calcular_pasaje(self, km):
        return 500 * km

class Metro(Transporte):
    def calcular_pasaje(self, km):
        return self.tarifa_fija

def main():
    bus = Bus(capacidad = 30, tarifa_fija = 3250)
    taxi = Taxi(capacidad = 4)
    metro = Metro(capacidad = 300, tarifa_fija = 3000)

    print("Costo para un trayecto de 10 km:")
    print("Bus:", bus.calcular_pasaje(10), "COP")
    print("Taxi:", taxi.calcular_pasaje(10), "COP")
    print("Metro:", metro.calcular_pasaje(10), "COP")

if __name__ == "__main__":
    main()
