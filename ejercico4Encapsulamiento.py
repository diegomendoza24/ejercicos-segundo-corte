class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.__edad = edad
        self.__documento = documento

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self.__edad = valor
        else:
            raise ValueError("La edad debe ser mayor o igual a 0")

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        self.__documento = valor


class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)
        self.__diagnostico = diagnostico
        self.__historial = []

    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    def ver_historial(self):
        return self.__historial

    def ver_diagnostico(self):
        return self.__diagnostico

    def _set_diagnostico(self, nuevo_diagnostico):
        self.__diagnostico = nuevo_diagnostico


class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        self.__especialidad = especialidad

    def ver_especialidad(self):
        return self.__especialidad

    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente._set_diagnostico(nuevo_diagnostico)
        else:
            raise TypeError("El objeto no es un Paciente")

if __name__ == "__main__":
    paciente1 = Paciente("Juan Pérez", 30, "12345678", "Gripe")
    paciente1.agregar_historial("Consulta inicial: síntomas leves de gripe.")
    paciente1.agregar_historial("Prescripción de medicamentos.")

    doctor1 = Doctor("Dra. García", 45, "87654321", "Medicina General")

    doctor1.modificar_diagnostico(paciente1, "Neumonía leve")

    print(f"Paciente: {paciente1.nombre}, Diagnóstico: {paciente1.ver_diagnostico()}")
    print(f"Historial médico: {paciente1.ver_historial()}")
    print(f"Doctor: {doctor1.nombre}, Especialidad: {doctor1.ver_especialidad()}")
