class HerenciaMultiple:
    def ejercicio31(self):
        print("HerenciaMultiple")


class ClaseA():

    def __init__(self, par1, par2):
        self.parametro1 = par1
        self.parametro2 = par2


class  ClaseB():

    def __init__(self, par3, par4, par5):
        self.parametro1 = par3
        self.parametro2 = par4
        self.parametro3 = par5


class ClaseX(ClaseA, ClaseB):
    pass

cX1 = ClaseX(15, 21)