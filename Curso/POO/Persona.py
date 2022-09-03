"""
¿En que consiste la programación Orienta a Objetos?
En traslador la naturaleza de los objetos de la vida real a codigo de programación
"""


class Persona:
    def ejercicio27(self):
        print("Persona")


class Persona():
    #Propiedades, caracteristicas o atributos:
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

# Funcionalidades:
    def despertar(self):
        self.despierta = True
        print("Buen dia.")

persona1 = Persona()
persona1.apellidos = "Sandoval Parra"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)


persona2 = Persona()
persona2.apellidos = "Aspiazu Peralta"
print(persona2.apellidos)
#persona2.despertar()
print(persona2.despierta)

