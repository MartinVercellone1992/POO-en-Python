# Herencia:

# Crea una clase base llamada Animal con atributos como nombre y edad. Luego, crea una subclase llamada Perro que herede de Animal y tenga un atributo adicional llamado raza. Crea un objeto de la clase Perro y muestra sus atributos.


class Animal:
    nombre = ""
    edad = ""

class Perro(Animal):
    raza = ""
    def __init__(self,nombre,edad,raza):
        self.nombre=nombre
        self.edad=edad
        self.raza=raza

    def mostrar(self):
        return f"\n{self.nombre}, {self.edad}, {self.raza}"

animal1 = Perro("Firualay", 7 , "Caschi")
animal2= Perro("Pancho", 12, "Delmo")
print(animal1.mostrar())
print(animal2.mostrar())