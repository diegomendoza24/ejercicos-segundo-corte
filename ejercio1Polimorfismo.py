class Transporte:
    def tipo_transporte(self):
        pass

class Coche(Transporte):
    def tipo_transporte(self):
        print("Transporte terrestre: Coche")

class Avion(Transporte):
    def tipo_transporte(self):
        print("Transporte aéreo: Avión")

class Barco(Transporte):
    def tipo_transporte(self):
        print("Transporte marítimo: Barco")

transportes = [Coche(), Avion(), Barco()]

for transporte in transportes:
    transporte.tipo_transporte()