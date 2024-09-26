class vehiculo():
    def __init__(self, marca = "", modelo = ""):
        self.marca = marca
        self.modelo = modelo
        
    def informacion(self):
        print(self.marca, self.modelo)
        
class coche(vehiculo):
    def __init__(self, marca="", modelo="", puertas = ""):
        super().__init__(marca, modelo)
        self.puertas = puertas
        
    def informacion(self):
        super().informacion()
        print(self.puertas)
        
    def encender(self):
        print("El coche está encendido")

        
class bicicleta(vehiculo):
    def __init__(self, marca="", modelo="", altura = ""):
        super().__init__(marca, modelo)
        self.altura = altura
        
    def informacion(self):
        super().informacion()
        print(self.altura)
        
    def modificarAltura(self, altura):
        self.altura = altura
        print("Altura modificada")
        
coche1 = coche("Ford", "Mondeo", "5")
bicicleta1 = bicicleta("Trek", "Full Carbon", "0.56")

coche1.encender()
bicicleta1.modificarAltura("0.60")