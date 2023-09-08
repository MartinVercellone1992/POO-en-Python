# Método __str__:

# Sobreescribe el método __str__ en la clase Persona para que al imprimir un objeto de la clase, muestre una representación más amigable de la persona (por ejemplo, "Nombre: Juan, Edad: 30").

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, nueva_edad):
        if nueva_edad < 0:
            print("La edad no puede ser un valor negativo.")
        else:
            self.edad = nueva_edad

persona = Persona("Martín", 30)
print(persona)