'''
6. Animales y edades
- Crea una clase `Animal` con atributos: especie, nombre, edad.
- Genere una lista de animales.
- Implementa un método que calcule el promedio de edades.
- Guarda y lee el archivo `animales.txt` mostrando los animales que superan la edad
promedio.
'''
class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"{self.especie} {self.nombre} {self.edad}"

    def promedio_edades(animales):
        edades = [animal.edad for animal in animales]
        promedio = sum(edades) / len(edades)
        return round(promedio)
          
animales = [
    Animal("Perro", "Firulais", 5),
    Animal("Gato", "Misu", 3),
    Animal("Loro", "Pepito", 2),
    Animal("Conejo", "Bunny", 1),
    Animal("Tortuga", "Manchas", 10),
    Animal("Caballo", "Relampago", 7),
    Animal("Hamster", "Copito", 1),
    Animal("Pez", "Nemo", 2)
]

edad_promedio = Animal.promedio_edades(animales)
print(f"Edad promedio: {edad_promedio}\n")

archivo = open(f"animales.txt", "w")
for animal in animales:
    archivo.write(str(animal) + "\n")
archivo.close()

print("Animales que superar el promedio")
archivo = open(f"animales.txt", "r")
for linea in archivo:
    datos = linea.strip().split()
    if int(datos[2]) > edad_promedio:
        print(f"Especie: {datos[0]}, Nombre: {datos[1]}, Edad: {datos[2]}")