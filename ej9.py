# Herencia Múltiple:

# Crea dos clases base, A y B, y luego crea una clase C que herede de ambas. Agrega métodos y atributos a las clases base y muestra cómo se heredan en la clase C.

class Empresa:
    def __init__(self,rango , funcion):
        self.rango = rango
        self.funcion = funcion
    def __str__(self):
        return f"\nPuesto: {self.rango}.\nFunción: {self.funcion}"

class Campos_de_trabajo:
    def __init__(self, turno, horas):
        self.turno = turno
        self.horas = horas
    def __str__(self):
        return f"\nAl turno {self.turno} le correspondes {self.horas}"

class Ingresos(Empresa, Campos_de_trabajo):
    def __init__(self, rango, funcion, turno, horas, paga):
        Empresa.__init__(self, rango, funcion)
        Campos_de_trabajo.__init__(self, turno, horas)
        self.paga = paga
    def __str__(self):
        return f"\nSe pagara {self.paga} dólaes por hora al {self.rango} del turno {self.turno}, en el puesto de {self.funcion}, cumpliendo {self.horas} al día."

personal = Ingresos("Técnico", "Diseño y  Desarrollo","Mañana", 6, 500)
print(personal)