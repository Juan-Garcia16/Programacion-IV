'''1. Realice un programa en el que podamos observar los atributos de las clases
inspiradas en el siguiente gráfico, se debe implementar herencia simple y se
deben guardar la información de cada vehículo en uno o varios archivos para
poder listarlos cuando se necesiten, el programa también debe contar con los
siguientes métodos:
- Métodos Vehículo:
a. Debe mostrar información dependiendo del vehículo (camión, moto,
automóvil) de cuantos años aproximadamente le pueden durar las llantas esto
también sujeto a tres tipos de marcas.
b. tipo de combustible que se recomienda usar para el vehículo que se elija
(ACPM, Extra, Corriente).
- Métodos Coche:
a. Mostrar que tiempo se tomaría cada vehículo en llegar desde Pereira a
diferentes lugares en Colombia (mínimo 5 lugares).
b. debe mostrar cuanto gastaría al mes en combustible cada automóvil
suponiendo que cada uno hace viajes de 1000 km mensuales, ustedes pueden
consultar precios actuales para parametrizar el combustible.'''
import json

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def vida_llantas(self, clase, marca):
        durabilidad = {
            "automovil": {"Bridgestone": 6, "Continental": 5, "Hankook": 4},
            "moto": {"Bridgestone": 4, "Continental": 3, "Hankook": 2},
            "camion": {"Bridgestone": 8, "Continental": 7, "Hankook": 5}
        }
        return durabilidad.get(clase.lower(), {}).get(marca, "No disponible")

    def tipo_combustible(self, clase):
        combustible = {
            "automovil": "Corriente",
            "moto": "Extra",
            "camion": "ACPM"
        }
        return combustible.get(clase.lower(), "Desconocido")


class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def tiempo_viaje(self, ciudad):
        distancias = {
            "Bogota": 320, "Cali": 215, "Medellin": 224,
            "Ibague": 125, "Cartago": 30, "Villavicencio": 386,
            "Santamarta": 1025
        }
        if ciudad not in distancias:
            return "Destino no registrado"
        return round(distancias[ciudad] / self.velocidad, 2)

    def gasto_mensual(self, precio_galon, rendimiento):
        galones = 1000 / rendimiento
        return round(galones * precio_galon, 2)


def guardar(coche, archivo="vehiculos_guardados.json"):
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
    except FileNotFoundError:
        datos = []

    datos.append(coche.__dict__)
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)


def listar(archivo="vehiculos_guardados.json"):
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
            for d in datos:
                print(d)
    except FileNotFoundError:
        print("No hay vehículos registrados.")


def main():
    auto = Coche(100, 1800, "Blanco", 4)
    print("\n--- Automovil ---")
    print("Duración llantas:", auto.vida_llantas("automovil", "Bridgestone"), "años")
    print("Combustible:", auto.tipo_combustible("automovil"))
    print("Tiempo a Bogotá:", auto.tiempo_viaje("Bogota"), "horas")
    print("Gasto mensual:", auto.gasto_mensual(13000, 40), "COP")
    guardar(auto)

    moto = Coche(60, 300, "Azul", 2)
    print("\n--- Moto ---")
    print("Duración llantas:", moto.vida_llantas("moto", "Continental"), "años")
    print("Combustible:", moto.tipo_combustible("moto"))
    print("Tiempo a Cali:", moto.tiempo_viaje("Cali"), "horas")
    print("Gasto mensual:", moto.gasto_mensual(15000, 100), "COP")
    guardar(moto)

    camion = Coche(50, 7000, "Plateado", 8)
    print("\n--- Camion ---")
    print("Duración llantas:", camion.vida_llantas("camion", "Hankook"), "años")
    print("Combustible:", camion.tipo_combustible("camion"))
    print("Tiempo a Santa Marta:", camion.tiempo_viaje("Santamarta"), "horas")
    print("Gasto mensual:", camion.gasto_mensual(11000, 15), "COP")
    guardar(camion)

    print("\nVehiculos guardados en 'vehiculos_guardados.json':")
    listar()


if __name__ == "__main__":
    main()
