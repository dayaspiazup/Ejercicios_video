class Cuenta:
    def ejercicio29(self):
        print("Cuenta")


class Cuenta():

    def __init__(self, pro, sal, non):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = non

    # Getters (métodos GET)
    def get_Saldo(self):
        return self.__saldo

    def get_Propietario(self):
        return self.__propietario

    def get_Moneda(self):
        return self.__moneda

    # Setters (métodos SET)
    def set_Moneda(self, moneda):
        self.__moneda = moneda


cuenta1 = Cuenta("Kevin Sandoval", 15000, "Soles")
print(cuenta1.get_Saldo())
print(cuenta1.get_Moneda())
cuenta1.set_Moneda("Dolares")
print(cuenta1.get_Moneda())