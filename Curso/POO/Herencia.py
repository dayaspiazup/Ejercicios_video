class Herencia:
    def ejercicio30(self):
        print("Herencia")


class Persona():

    def __init__(self, apePat, apeMat, nom ):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno,self.apellidoMaterno, self.nombres)

    def datos(self):
        print(self.mostrarNombreCompleto())

class Estudiante(Persona):

    def __init__(self,apePat, apeMat, nom, pro):
        super().__init__(apePat, apeMat, nom)
        self.profesión = pro


    def datos(self):
        super().datos()
        print("Profesión: {0}".format(self.profesión))


#estu1 = Estudiante("Peralta", "Campoverde", "Jorge", "Ingeniería Industrial")
per1 = Persona("Peralta", "Campoverde", "Jorge")
#print(estu1.mostrarNombreCompleto())
#print(estu1.profesión)
#estu1.datos()

print(isinstance(per1, Estudiante)) 
