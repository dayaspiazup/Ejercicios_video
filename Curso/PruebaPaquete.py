"""
Paquetes:
Directorios (carpetas) donde se almacenan modulos relacionados entre si.

¿Para qué sirven?
Para organizar mejor el codigo y poder reutilizar mejor.

¿Como se crea un paquete?
Crea una carpeta o directorio con un archivo dentro llamado __init__.py
"""
from Paquete1.FuncionesCadena import contarLetras
from Paquete1.FuncionesNumericas import *

print(multiplicar(5, 6))
print(contarLetras("ServiChocli"))