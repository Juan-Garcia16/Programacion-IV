'''
5. Clasificación de objetos electrónicos
- Crea una clase `Electrodomestico` con atributos: nombre, marca, consumo (en
watts).
- Implemente un método que clasifique los objetos como “bajo consumo” (<500W) o
“alto consumo” (>=500W).
- Guarda el inventario en `electrodomesticos.txt`.
'''
class Electrodomestico:
    def __init__(self, nombre, marca, consumo_watts):
        self.nombre = nombre
        self.marca = marca
        self.consumo_watts = consumo_watts
        
    def __str__(self):
        return f"{self.nombre} {self.marca} {self.consumo_watts}W "
        
    def clasificacion(lista_electrodomesticos, archivo = "electrodomesticos.txt"):
        archivo = open(archivo, "w")
        for electrodomestico in lista_electrodomesticos:
            if electrodomestico.consumo_watts < 500:
                archivo.write(str(electrodomestico) + "BAJO CONSUMO\n")
            else:
                archivo.write(str(electrodomestico) + "ALTO CONSUMO\n")
        archivo.close()
        print("Inventario guardado en 'electrodomesticos.txt'")
                
electrodomesticos = [Electrodomestico("Lavadora", "Samsung", 700),
                     Electrodomestico("Televisor", "LG", 450),
                     Electrodomestico("Bafle", "Sony", 500),
                     Electrodomestico("Microondas", "Panasonic", 300),
                     Electrodomestico("Nevera", "Samsung", 750)]

Electrodomestico.clasificacion(electrodomesticos)
