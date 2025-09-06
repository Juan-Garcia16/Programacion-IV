'''
Cree una clase “Triangulo” donde me calcule área, perímetro y un método que me
diga que tipo de triangulo es.
'''

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def es_valido(self):
        #verifica la desigualdad triangular para determinar si es un triangulo valido
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def area(self):
        if self.es_valido():
            #frmula de Heron
            s = (self.lado1 + self.lado2 + self.lado3) / 2
            area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
            return area
        else:
            return None

    def perimetro(self):
        if self.es_valido():
            return self.lado1 + self.lado2 + self.lado3
        else:
            return None

    def tipo_triangulo(self):
        if not self.es_valido():
            return "No es un triangulo valido"
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


lado1 = float(input("Ingrese el valor del primer lado del triángulo: "))
lado2 = float(input("Ingrese el valor del segundo lado del triángulo: "))
lado3 = float(input("Ingrese el valor del tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

if triangulo.es_valido():
    print(f"Area del triangulo: {triangulo.area():.2f}")
    print(f"Perímetro del triangulo: {triangulo.perimetro()}")
    print(f"Tipo de triangulo: {triangulo.tipo_triangulo()}")
else:
    print("Los lados ingresados no forman un triangulo valido")
