'''
3. Define una clase base Figura con un método area().
Implementa subclases Rectangulo, Triangulo y Circulo que sobrescriban el método
area() con la fórmula correspondiente.
Crea objetos de cada clase y guarda sus áreas en una lista. Luego recórrela
mostrando qué tipo de figura es y cuánto mide su área.
'''
class Figura:
    def area(self):
        return 0

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14 * (self.radio ** 2)

def main():
    figuras = [
        Rectangulo(4, 5),
        Triangulo(3, 6),
        Circulo(2)
    ]

    for f in figuras:
        print(f"{type(f).__name__}, area = {f.area()}")

if __name__ == "__main__":
    main()
