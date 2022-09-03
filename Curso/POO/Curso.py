class Curso:
    def ejercicio28(self):
        print("Curso")


class Curso ():
    """
    nombre = "Fisica"
    creditos = 6
    profesion = "Ingenieria Industrial"
    """

# Estado inicial del objeto
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.créditos = cre
        self.profesión = pro
        self.__impartición = "Presencial"  #Propiedad encapsulada.

    def mostrarDatos(self):
        dat = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
        print(dat.format(self.nombre, self.créditos, self.__impartición))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asignado.")
        else:
            print("No es necesario asignar un docente...")


    def __verificarDocente(self):
        print("Verificar si existe docente asignado..")
        if self.__impartición == "Presencial":
            return  True
        else:
            return False

    # toString()
    def __str__(self):
        texto = "Nombre: {0} - Créditos: {1} "
        return texto.format(self.nombre, self.créditos)


curso1 = Curso("Física", 6, "Ingenieria Industrial")
print(curso1)
curso1.mostrarDatos()



#curso2 =curso("Biologia", 3, "Ingenieria Civil")
#print(curso2.nombre)
