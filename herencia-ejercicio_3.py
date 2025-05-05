class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Año: {self.año}")

class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo

    def mostrar_informacion_coche(self):
        super().mostrar_informacion()
        print(f"Modelo: {self.modelo}")

coche1 = Coche("Toyota", 2022, "Corolla")
coche2 = Coche("Ford", 2021, "Focus")

coche1.mostrar_informacion_coche()
print()
coche2.mostrar_informacion_coche()
