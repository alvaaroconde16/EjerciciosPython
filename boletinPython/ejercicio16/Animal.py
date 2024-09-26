class animal():
    def hablar(self):
        print("Soy un animal")
        
class perro(animal):
    def hablar(self):
        print("Soy un perro")
        
class gato(animal):
    def hablar(self):
        print("Soy un gato")
        
animal1 = animal()
perro1 = perro()
gato1 = gato()

animal1.hablar()
perro1.hablar()
gato1.hablar()