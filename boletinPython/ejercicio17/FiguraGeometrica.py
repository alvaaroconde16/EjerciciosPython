class figuraGeometrica():
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def calcularArea(self):
        return 0
    
class rectangulo(figuraGeometrica):
    def __init__(self, ancho, altura):
        super().__init__(ancho, altura)
        
    def calcularArea(self):
        return self.ancho * self.altura
    
class triangulo(figuraGeometrica):
    def __init__(self, ancho, altura):
        super().__init__(ancho, altura)
        
    def calcularArea(self):
        return (self.ancho * self.altura)/2
    
rectangulo1 = rectangulo(5, 6)
triangulo1 = triangulo(5, 2)

print("El área del rectángulo es: " + str(rectangulo1.calcularArea()))
print("El área del triángulo es: " + str(triangulo1.calcularArea()))