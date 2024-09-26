class empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_salario_anual(self):
        return print("El salario anual es de " + str(self.salario))
    
class gerente(empleado):
    def __init__(self, nombre, salario, cargo):
        super().__init__(nombre, salario)
        self.cargo = cargo
        
    def calcular_salario_anual(self):
        return super().calcular_salario_anual()
    
    def cerrarProyecto(self):
        print("Proyecto cerrado")
        
class programador(empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
        
    def calcular_salario_anual(self):
        return super().calcular_salario_anual()
    
    def añadirLenguaje(self, lenguaje):
        self.lenguaje = lenguaje
        print("Lenguaje añadido")
        

gerente1 = gerente("Luis", "4000", "Super")
programador1 = programador("Pepi", "2500", "Python")

gerente1.calcular_salario_anual()
gerente1.cerrarProyecto()

programador1.calcular_salario_anual()
programador1.añadirLenguaje("Java")