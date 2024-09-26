class cuentaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositarDinero(self, saldo):
        self.saldo += saldo
        print("Dinero depositado")
        
    def retirarDinero(self, saldo):
        self.saldo -= saldo
        print("Dinero retirado")
        
        
persona1 = cuentaBancaria("Alberto", 4000)

print("Saldo: " + str(persona1.saldo))

persona1.depositarDinero(20)
print("Saldo: " + str(persona1.saldo))

persona1.retirarDinero(120)
print("Saldo: " + str(persona1.saldo))