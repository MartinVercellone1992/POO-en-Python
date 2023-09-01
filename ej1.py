# Crear una clase básica:

# Crea una clase llamada Persona que tenga dos atributos: nombre y edad. Luego, crea dos objetos de esta clase e imprime sus atributos.

class Persona:
    nombre = ""
    edad = ""

Persona1 = Persona()
Persona2 = Persona()

Persona1.nombre = "Jorge"
Persona1.edad = 38

Persona2.nombre = "Marcela"
Persona2.edad = 44

print (Persona1.nombre, Persona1.edad)
print (Persona2.nombre, Persona2.edad)
