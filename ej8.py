# Composición:

# Crea una clase CuentaBancaria que tenga un saldo y un titular (un objeto de la clase Persona). Luego, crea una instancia de CuentaBancaria y asocia una persona a ella. Implementa métodos para depositar y retirar dinero de la cuenta.

class Persona:
    def __init__(self,nomrbe, edad):
        self.nombre = nomrbe
        self.edad = edad
    def __str__(self):
        return f"\nNombre: {self.nombre}, Edad: {self.edad}"

class Cuenta_bancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"\nSe ha depositado ${cantidad} en la cuenta {self.titular}")
        else: print("\nNo se ha depositado dinero.")
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"\nSe retiro ${cantidad} de la cuenta {self.titular}.\nSu saldo es de ${self.saldo}.")
        elif cantidad <= 0:
            print("Error...!!!")
        else: print(f"\nFondos insuficientes.\nSu saldo es de ${self.saldo}.")

Martin = Persona("Martín", 30)
cuenta_Martin = Cuenta_bancaria("Martín", 300000)

print(Martin)
cuenta_Martin.depositar(150)
print(f"Su saldo es de:${cuenta_Martin.saldo}")
cuenta_Martin.retirar(75)
