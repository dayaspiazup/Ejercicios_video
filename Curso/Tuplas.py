class Tuplas:
    def ejercicio7(self):
        print("Tuplas")


tupla =(1, 2, 3)
print(tupla)
tupla2 = (8, "Xiomara", True, 20.21, 32+ 9j, 24 + 20j, 19, "Alegria", False)
print(tupla2)
tupla3 = (10, 24, (3, 8, 7))
print(tupla3)
print(tupla2[1])
# tupla2[1] = "Xiomara"
print(tupla2[-1]) # Acceder al último elemento.
print(tupla2[0:4])
print(tupla2[-2])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaFinal = tupla + tupla3
print(tuplaFinal)

print(tuplaFinal.count(22))
print(tuplaFinal.index(3))