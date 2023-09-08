class Aspiradora:
    """Class representing a person"""

    def __init__(self):
        self.x = 0
        self.y = 0

    def limpiar(self, entorno):
        if entorno[self.x][self.y] == "Sucio":
            entorno[self.x][self.y] = "Limpio"

    def moverse(self, entorno):
        if self.x < len(entorno)-1 and self.y % 2 == 0:
            self.x += 1
        elif self.x > 0 and self.y % 2 != 0:
            self.x -= 1
        elif self.y == len(entorno)-1:
            self.y = 0
        else:
            self.y += 1

ent = [["Sucio", "Limpio", "Sucio"],
       ["Limpio", "Sucio", "Limpio"],
       ["Limpio", "Sucio", "Limpio"]]

def Mostrar_Entorno(entorno):
    print("\n")
    for fila in entorno:
        for elemento in fila:
            print(elemento + ", ")
        print("\n")
    print("----------------------------------")
aspiradora = Aspiradora()

Mostrar_Entorno(ent)
for fila in ent:
    for elemento in fila:
        aspiradora.limpiar(ent)
        aspiradora.moverse(ent)
Mostrar_Entorno(ent)