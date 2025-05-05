class Persona:
 def __init__(self, nombre, edad):
   self.nombre = nombre
   self.edad = edad
   
 def mostrar_info(self):
        print(f"nombre: {self.nombre}, edad: {self.edad}")
   
class Estudiante(Persona):
   def __init__(self, nombre, edad, grado):
     super().__init__( nombre, edad)
     self.grado = grado 

def grado_estudiante(self):
     print(f"El grado del estudiante {self.nombre} es: {self.grado}")

Juan = Estudiante("Juan", 20, "2 grado")
print(Juan.nombre)
print(Juan.edad)
print(Juan.grado)

Diego = Estudiante("Diego", 24, "1 grado")
print(Diego.nombre)
print(Diego.edad)
print(Diego.grado)