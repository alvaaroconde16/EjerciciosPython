class estudiante():
    def __init__(self, nombre = "", edad = "", curso = ""):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        
estudiante1 = estudiante("Juan Carlos", "24", "2A")
estudiante2 = estudiante("Maria", "18", "6C")
estudiante3 = estudiante("Andrea", " 20", "4B")

lista = [estudiante1, estudiante2, estudiante3]

for x in lista:
    print(str(x.nombre), end=", ") 
    print(str(x.edad), end = ", ")
    print(str(x.curso))