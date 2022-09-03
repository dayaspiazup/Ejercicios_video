class Cadenas:
    def ejercicio6(self):
        print("Cadenas")


texto = "BienVenidos a la pagina de Xiomara"

print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title()) # Convierte una cadena a un formato de título
print(texto.find("la")) # Posición donde se encuentra la cadena o porción
print(texto.count("a")) # Cantidad de ocurrencias de una letra o porción

textoFinal = texto.replace("a","6")
print(textoFinal)

valor = texto.isnumeric() # Arroja true o false dependiendo si es un número
print(valor)

cadenaSeparada = texto.split(" ")
print(cadenaSeparada)