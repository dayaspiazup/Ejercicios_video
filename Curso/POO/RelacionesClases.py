class RelacionesClases:
    def ejercicio33(self):
        print("RelacionesClases")


class País():

    def __init__(self, nom, pre):
        self.nombre = nom
        self.presidente = pre


    def __str__(self):
        txt = "País:{0} - Presidente:{1}"
        return  txt.format(self.nombre, self.presidente)

class Ciudad():

    def __init__(self, nom, hab, paí):
        self.nombre = nom
        self.habitantes = hab
        self.país = paí

    def __str__(self):
        txt = "Ciudad: {0} -Nº Habitantes: {1} ({2})"
        return txt.format(self.nombre, self.habitantes, self.país)


class Urbanización():

    def __init__(self, nom, ciu):
        self.nombre = nom
        self.ciudad = ciu

    def __str__(self):
        txt = "Urbanización: {0} ({1}) "
        return txt.format(self.nombre, self.ciudad)


país1 = País("Ecuador", "Guillermo Lasso")
print(país1)

ciudad1 = Ciudad("Naranjito", 16000, país1)
print(ciudad1)

urba1 = Urbanización("Campo Abierto", ciudad1)
print(urba1)