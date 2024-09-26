class rectangulo():
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
        
    def calcularArea(self):
        return self.ancho * self.altura
    
    def calcularPerimetro(self):
        return (self.ancho * 2) + (self.altura * 2)
    

rectangulo1 = rectangulo(5,6)

print("Área: " + str(rectangulo1.calcularArea()))
print("Perímetro: " + str(rectangulo1.calcularPerimetro()))