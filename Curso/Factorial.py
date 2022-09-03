class Factorial:
    def ejercicio18(self):
        print("Factorial")


numero = int(input("Ingrese un numero: "))

factorial = 1
for n in range(1, (numero + 1)):
    factorial = factorial * n

print(("El factorial de {0} es: {1} ".format(numero, factorial)))
