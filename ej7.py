# Métodos estáticos:
# Agrega un método estático llamado es_mayor_de_edad() en la clase Persona que tome una edad como parámetro y devuelva True si la persona es mayor de 18 años, y False en caso contrario. Llama a este método con diferentes edades para comprobar su funcionamiento.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"\nNombre: {self.nombre}, Edad: {self.edad}\n"

    def __del__(self):
        print(f"Se ha destruido a la persona: {self.nombre}")
        print(f"Se ha destruido a la persona: {self.edad}")

    def get_edad(self):
        return self.edad


persona = Persona("Martín", 30)
persona2 = Persona("Luis", 35)

print(persona)
print(persona2)
