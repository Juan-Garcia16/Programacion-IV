'''
4. Diseñe una clase `Vehículo` que guarde marca, modelo, año, tipo y placa. Incluya un
método para guardar en archivo solo los vehículos del año actual y otro para leerlos.
'''
class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo, placa):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = tipo
        self.placa = placa
        
    def __str__(self):
        return f"{self.marca},{self.modelo},{self.anio},{self.tipo},{self.placa}"
    
    def guardar_vehiculos_anio_actual(self, nombre_archivo):
        with open(nombre_archivo, "a") as archivo:
            if self.anio == 2025:
                archivo.write(str(self) + "\n")
    
    def leer_vehiculos_anio_actual(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            lectura = archivo.readlines()
        return lectura
            
vehiculos = [
    Vehiculo("Toyota", "Corolla", 2020, "Automóvil", "ABC123"),
    Vehiculo("Honda", "Civic", 2025, "Automóvil", "XYZ789"),
    Vehiculo("Ford", "Ranger", 2022, "Camioneta", "JKL456"),
    Vehiculo("Yamaha", "MT-07", 2021, "Motocicleta", "MOTO77"),
    Vehiculo("Chevrolet", "Spark", 2025, "Automóvil", "CHEV19"),
    Vehiculo("Mercedes-Benz", "Sprinter", 2025, "Camión", "SPR2023"),
    Vehiculo("Kawasaki", "Ninja 650", 2020, "Motocicleta", "KWK650"),
    Vehiculo("Hyundai", "Tucson", 2021, "SUV", "HYD321"),
    Vehiculo("Mazda", "CX-5", 2025, "SUV", "MZD555"),
    Vehiculo("Volkswagen", "Jetta", 2025, "Automóvil", "VWJ717")
]

for vehiculo in vehiculos:
    vehiculo.guardar_vehiculos_anio_actual('vehiculos.txt')

vehiculos_2025 = Vehiculo.leer_vehiculos_anio_actual('vehiculos.txt')
    
print("\nVehiculos del año 2025 guardados en 'vehiculos.txt':\n")
for vehiculo in vehiculos_2025:
    print(vehiculo.strip())
            

    
    