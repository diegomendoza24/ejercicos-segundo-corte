class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base

    def get_sueldo_base(self):
        return self.__sueldo_base

    def set_sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            print("El sueldo no puede ser negativo.")

    def calcular_salario(self):
        return self.__sueldo_base

class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return self.get_sueldo_base()

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, sueldo_base, dias_trabajados, pago_por_dia):
        super().__init__(nombre, sueldo_base)
        self.dias_trabajados = dias_trabajados
        self.pago_por_dia = pago_por_dia

    def calcular_salario(self):
        return self.dias_trabajados * self.pago_por_dia

if __name__ == "__main__":
    empleados = [
        EmpleadoFijo("Ana", 3000),
        EmpleadoPorHoras("Luis", 0, horas_trabajadas=120, pago_por_hora=25),
        EmpleadoTemporal("María", 0, dias_trabajados=15, pago_por_dia=100)
    ]

    for empleado in empleados:
        print(f"Empleado: {empleado.nombre}, Salario calculado: ${empleado.calcular_salario()}")
