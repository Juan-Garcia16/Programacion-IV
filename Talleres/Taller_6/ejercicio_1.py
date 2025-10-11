'''
1. Realice un programa para calcular diferentes áreas al menos 4 áreas de
figuras trigonométricas haciendo uso de clases y herencia se puede realizar
el modelamiento, deben encapsular todos los atributos y métodos, cuando
diseñen el set de cada atributo deben tener en cuenta dentro de este
método set que solo se deben ingresar números positivos.
'''
import math

class Figura:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")
    
    def area(self):
        pass


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.set_base(base) # evita validaciones extras al momento de crear la instancia
        self.set_altura(altura)
    
    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura
    
    def set_base(self, base):
        if isinstance(base, (int, float)) and base > 0:
            self.__base = base
        else:
            raise ValueError("La base del triángulo debe ser un número positivo")

    def set_altura(self, altura):
        if isinstance(altura, (int, float)) and altura > 0:
            self.__altura = altura
        else:
            raise ValueError("La altura del triángulo debe ser un número positivo")
    
    def area(self):
        return (self.__base * self.__altura) / 2


class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.set_lado(lado)
    
    def get_lado(self):
        return self.__lado
    
    def set_lado(self, lado):
        if isinstance(lado, (int, float)) and lado > 0:
            self.__lado = lado
        else:
            raise ValueError("El lado del cuadrado debe ser un número positivo")
    
    def area(self):
        return self.__lado ** 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.set_base(base)
        self.set_altura(altura)
    
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    def set_base(self, base):
        if isinstance(base, (int, float)) and base > 0:
            self.__base = base
        else:
            raise ValueError("La base del rectángulo debe ser un número positivo")
    
    def set_altura(self, altura):
        if isinstance(altura, (int, float)) and altura > 0:
            self.__altura = altura
        else:
            raise ValueError("La altura del rectángulo debe ser un número positivo")
    
    def area(self):
        return self.__base * self.__altura


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.set_radio(radio)
    
    def get_radio(self):
        return self.__radio
    
    def set_radio(self, radio):
        if isinstance(radio, (int, float)) and radio > 0:
            self.__radio = radio
        else:
            raise ValueError("El  del circulo debe ser un número positivo")
    
    def area(self):
        return math.pi * (self.__radio ** 2)


def main():
    print("--- ÁREAS DE FIGURAS GEOMETRICAS ---\n")

    triangulo = Triangulo(5, 3)
    cuadrado = Cuadrado(4)
    rectangulo = Rectangulo(6, 2)
    circulo = Circulo(3)

    figuras = [triangulo, cuadrado, rectangulo, circulo]

    for f in figuras:
        print(f"{f.get_nombre()} -> Área: {round(f.area(), 2)}")
        
if __name__ == "__main__":
    main()
