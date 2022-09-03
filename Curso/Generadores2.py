"""
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng
"""


class Generadores2:
    def ejercicio22(self):
        print("Generadores2")


def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng

lemguajesObtenidos = devuelveLenguajes("Python", "Java", "HP", "Ruby", "JavaScript")

print(next(lemguajesObtenidos))
print(next(lemguajesObtenidos))