'''
• Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehículos.
• Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra
mostrando el nombre de su clase y sus atributos.
• Modifica la función catalogar() para que reciba un argumento optativo ruedas,
haciendo que muestre únicamente los que su número de ruedas concuerde con el
valor del argumento. También debe mostrar un mensaje "Se han encontrado {}
vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a
prueba con 0, 2 y 4 ruedas como valor.
'''

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"{self.__class__.__name__} | Color: {self.color}, Ruedas: {self.ruedas}"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad_max, motor_cc):
        super().__init__(color, ruedas)
        self.velocidad_max = velocidad_max
        self.motor_cc = motor_cc

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad_max} km/h, Motor: {self.motor_cc} cc"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, categoria):
        super().__init__(color, ruedas)
        self.categoria = categoria

    def __str__(self):
        return super().__str__() + f", Categoría: {self.categoria}"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad_max, motor_cc, carga_kg):
        super().__init__(color, ruedas, velocidad_max, motor_cc)
        self.carga_kg = carga_kg

    def __str__(self):
        return super().__str__() + f", Capacidad de carga: {self.carga_kg} kg"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, categoria, velocidad_max, motor_cc):
        super().__init__(color, ruedas, categoria)
        self.velocidad_max = velocidad_max
        self.motor_cc = motor_cc

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad_max} km/h, Motor: {self.motor_cc} cc"


def catalogar(vehiculos, ruedas=None):
    encontrados = 0
    for v in vehiculos:
        if ruedas is None or v.ruedas == ruedas:
            print(v)
            if ruedas is not None:
                encontrados += 1

    if ruedas is not None:
        print(f"\nSe encontraron {encontrados} vehiculos con {ruedas} ruedas")


def main():
    vehiculos = [
        Coche("Rojo", 4, 180, 1600),
        Bicicleta("Azul", 2, "Montaña"),
        Camioneta("Negra", 4, 160, 2000, 1200),
        Motocicleta("Blanca", 2, "Deportiva", 220, 600),
        Vehiculo("Gris", 0)
    ]

    print("-- Catalogo completo --")
    catalogar(vehiculos)

    print("\n-- Vehiculos con 0 ruedas --")
    catalogar(vehiculos, 0)

    print("\n-- Vehiculos con 2 ruedas --")
    catalogar(vehiculos, 2)

    print("\n-- Vehiculos con 4 ruedas --")
    catalogar(vehiculos, 4)

if __name__ == "__main__":
    main()
