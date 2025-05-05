class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}")

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.raza = raza

    def mostrar_informacion_perro(self):
        super().mostrar_informacion()
        print(f"Raza: {self.raza}")

perro1 = Perro("Rex", "Canino", "Pastor Alemán")
perro2 = Perro("Luna", "Canino", "Golden Retriever")
perro3 = Perro("Max", "Canino", "Bulldog Francés")

perro1.mostrar_informacion_perro()
print()
perro2.mostrar_informacion_perro()
print()
perro3.mostrar_informacion_perro()
