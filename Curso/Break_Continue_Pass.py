"""
for numero in range(1, 6):
    if numero == 3:
        break  # Descanso o interrupción en este punto.
    print("El número es: {0}".format(numero))

print("Bucle terminado.")
"""

# Continue: Omite una parte del bucle cuando se cumple una condición y
# continúa con el resto.
"""
for numero in range(1, 6):
    if numero == 3: # Continua con el resto del bucle.
        continue
    print("El número es: {0}".format(numero))

print("Bucle terminado.")
"""
# Pass: Permite continuar con una secuencia o función que ya no tiene
# o agún no tiene un bloque de código útil.

class Break_Continue_Pass:
    def ejercicio20(self):
        print("Break_Continue_Pass")


for numero in range(1, 6):
    if numero <= 3:
        # Aquí no pasa nada y el bucle sigue trabajo
        pass
    else:
        print("El siguiente valor es mayor a 3:")
    print("El número es: {0}".format(numero))

print("Bucle terminado.")

def funcionSinImplementar():
    pass

