# Polimorfismo:

# Crea una clase base Figura con un método calcular_area(). Luego, crea subclases como Circulo y Rectangulo que sobreescriban el método calcular_area() para calcular el área de su forma específica. Luego, crea objetos de cada subclase y llama al método calcular_area() en cada uno.

import math

class Figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__(0,0)
        self.radio = radio
    def calcular_area(self):
        return math.pi * self.radio**2

class Rectangulo(Figura):
    def calcular_area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def calcular_area(self):
        return (self.base * self.altura)/2
        

circulo = Circulo(5)
area_circulo = circulo.calcular_area()
cuadrado = Cuadrado(4)
area_cuadrado = cuadrado.calcular_area()
rectangulo = Rectangulo(4,3)
area_rectangulo = rectangulo.calcular_area()
triangulo = Triangulo(6,3)
area_triangulo = triangulo.calcular_area()


print (f"\nEl area del circulo es: {area_circulo:.2f}")
print (f"El area del cuadrdo es: {area_cuadrado}")
print (f"El area del rectángulo es: {area_rectangulo}")
print (f"El area del triángulo es: {area_triangulo}")
