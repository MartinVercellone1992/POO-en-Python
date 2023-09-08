# Métodos de clase:

# Modifica la clase Persona para que tenga un método llamado saludar() que imprima un saludo usando el nombre de la persona. Crea un objeto de la clase y llama a este método.

class Persona:
    nombre = ""
    edad = ""

    def Saludar(self):
        print(f"Hola {self.nombre}")

Persona1 = Persona()
Persona2 = Persona()

Persona1.nombre = "Jorge"
Persona1.edad = 38

Persona2.nombre = "Marcela"
Persona2.edad = 44

Persona1.Saludar()
Persona2.Saludar()
