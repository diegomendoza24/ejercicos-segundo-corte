class Empleado:
    def __init__(self, nombre, rol, clave):  
        self.__nombre = nombre
        self.__rol = rol
        self._clave_acceso = self.__cifrar_clave(clave)

    def __cifrar_clave(self, clave):
        """Cifra la clave invirtiéndola."""
        return clave[::-1]

    def __descifrar_clave(self, clave_cifrada):
        """Descifra la clave invertida."""
        return clave_cifrada[::-1]

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rol(self):
        return self.__rol

    def verificar_clave(self, clave_ingresada):
        """Verifica si la clave ingresada es correcta."""
        return self.__cifrar_clave(clave_ingresada) == self._clave_acceso

    def cambiar_clave(self, clave_antigua, nueva_clave):
        """Permite cambiar la clave solo si la antigua clave es correcta."""
        if self.verificar_clave(clave_antigua):
            self._clave_acceso = self.__cifrar_clave(nueva_clave)
            print("Clave actualizada exitosamente.")
        else:
            print("La clave antigua es incorrecta. No se puede cambiar la clave.")

empleado1 = Empleado("Ana Rodríguez", "Administrador", "secreto123")

print(f"Nombre: {empleado1.nombre}")
print(f"Rol: {empleado1.rol}")
print(f"¿Clave 'secreto123' correcta?: {empleado1.verificar_clave('secreto123')}")
print(f"¿Clave 'incorrecta' correcta?: {empleado1.verificar_clave('incorrecta')}")

empleado1.cambiar_clave("secreto123", "nuevaClave456")
print(f"¿Nueva clave 'nuevaClave456' correcta?: {empleado1.verificar_clave('nuevaClave456')}")
empleado1.cambiar_clave("secreto123", "otraClave")
