class For:
    def ejercicio17(self):
        print("For")


for i in range(1, 13):
    print("{0} x {1} es: {2}".format(i, i, (i * i) ))

for nom in ["Maria", "Narcisa", "Lourdes", "Rosa"]:
    print("Cantidad de letra de {0} es: {1}".format(nom, len(nom)))