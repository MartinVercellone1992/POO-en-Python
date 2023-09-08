# Constructor y Destructor:

# Agrega un constructor (__init__) y un destructor (__del__) a la clase Persona para imprimir mensajes cuando se cree y destruya un objeto de la clase.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def __del__(self):
        print(f"Se a destruido a la persona: {self.nombre} ")
    
    def get_edad(self):
        return self.edad

persona1 = Persona("Martín", 30)
persona2 = Persona("Jorje", 58)

print(persona1)
del persona2