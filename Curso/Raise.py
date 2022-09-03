class Raise:
    def ejercicio24(self):
        print("Raise")


def evaluarNota(nota):
    if nota < 0:
        raise ValueError("Valor incorrecto.")
        #raise ZeroDivisionError("Este personaje es personalizado.")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")

evaluarNota(7)

print("Este es el fin de mi programa")