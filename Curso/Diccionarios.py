class Diccionarios:
    def ejercicio9(self):
        print("Diccionarios")


miDiccionario = {"Alemania": "Berlin", "España": "Madrid", "Perú": "Lima"}
print(miDiccionario["Perú"])
print(miDiccionario)

miDiccionario["Venezuela"] = "Caracas"
print(miDiccionario)

miDiccionario["España"] = "Barcelona"
print(miDiccionario)

del miDiccionario["España"]
print(miDiccionario)

dic2 = {"Aspiazu": "Dayana", 19: True, "Sueldo": 152.70}
print(dic2[19])

llaves = ("España", "Francia", "Inglaterra")
dicPaises ={llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"}
print(dicPaises)

datosPersonales ={"Ape": "Aspiazu", "Anios": {1:2016, 2:2017, 3:2018, 4:2019, 5:2020,}}
print(datosPersonales)
print(datosPersonales["Anios"])

print(datosPersonales.get('Ape', "Dayana"))


print(datosPersonales.keys())
valores = tuple(datosPersonales.values())
print(valores)

