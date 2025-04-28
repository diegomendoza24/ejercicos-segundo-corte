class Estudiante:
    def __init__(self, nombre, codigo): 
        self.__nombre = self.validar_nombre(nombre)
        self.__codigo = self.validar_codigo(codigo)
        self.__notas = []

    def validar_nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        return nombre

    def validar_codigo(self, codigo):
        if not str(codigo).isalnum():
            raise ValueError("El código debe ser alfanumérico.")
        return codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = self.validar_nombre(nuevo_nombre)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = self.validar_codigo(nuevo_codigo)

    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            print("La nota debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self):
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)  
        else:
            return 0.0

    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0

estudiante1 = Estudiante("Carlos López", "CL456")
estudiante2 = Estudiante("Sofía Gómez", "SG789")
estudiante3 = Estudiante("Mateo Vargas", "MV012")

estudiante1.agregar_nota(3.5)
estudiante1.agregar_nota(4.0)
estudiante2.agregar_nota(4.8)
estudiante2.agregar_nota(4.5)
estudiante3.agregar_nota(2.5)
estudiante3.agregar_nota(3.2)

print(f"Nombre: {estudiante1.nombre}, Código: {estudiante1.codigo}, Promedio: {estudiante1.calcular_promedio():.2f}, ¿Aprobado?: {estudiante1.es_aprobado()}")
print(f"Nombre: {estudiante2.nombre}, Código: {estudiante2.codigo}, Promedio: {estudiante2.calcular_promedio():.2f}, ¿Aprobado?: {estudiante2.es_aprobado()}")
print(f"Nombre: {estudiante3.nombre}, Código: {estudiante3.codigo}, Promedio: {estudiante3.calcular_promedio():.2f}, ¿Aprobado?: {estudiante3.es_aprobado()}")
