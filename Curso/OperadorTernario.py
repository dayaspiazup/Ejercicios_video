class OperadorTernario:
    def ejercicio14(self):
        print("OperadorTernario")


sexos = ("Hombre", "Mujer")

posicion = True
sexo = sexos[posicion] # Mujer
print(sexo)
sexo = sexos[not posicion] # Hombre
print(sexo)