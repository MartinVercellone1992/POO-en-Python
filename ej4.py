# Encapsulación:

# Agrega métodos get y set para los atributos de la clase Persona para acceder y modificar la edad de una persona de manera segura.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def  get_edad(self):
        return self.edad
    
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.edad = nueva_edad
        
        else:
            print("La edad no puede ser un valor negativo.")

persona = Persona("Martín" , 30)

print(persona.get_edad())
persona.set_edad(32)
print(persona.get_edad())