class Listas:
    def ejercicio8(self):
        print("Listas")


lista1 = ["Xiomara", 24, 99.1,True, "Kevin",19.20]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])


print(lista1[0:3])
print(lista1[:2])
print(lista1[3:])

lista1.append("Xiomara")
print(lista1)

lista1.insert(5, "Ecuador")
print(lista1)

lista1.extend(["Kevin", 120, False])
print(lista1)

print(lista1.index("Kevin"))

lista1.remove(19.2)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["Naranjito", "Santiago"]
lista3 = lista1 + lista2
print(lista3)

print(lista2 * 4)

print("Xiomara" in lista1)
