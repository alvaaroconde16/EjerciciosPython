class coche():
    def __init__(self, marca = "", modelo = ""):
        self.marca = marca
        self.modelo = modelo
        
    def mostrarInformacion(self):
        print(self.marca, self.modelo)
        
coche1 = coche("Seat", "León")
coche2 = coche("Ford", "Mondeo")

coche1.mostrarInformacion()
coche2.mostrarInformacion()