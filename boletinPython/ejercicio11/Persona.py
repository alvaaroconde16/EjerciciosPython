class persona():
    def __init__(self, nombre = "", edad = ""):
        self.nombre = nombre
        self.edad = edad
        
persona1 = persona("Sergio", "24")

print("Nombre: " + persona1.nombre)
print("Edad: " + persona1.edad)