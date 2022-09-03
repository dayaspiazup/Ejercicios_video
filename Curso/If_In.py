class If_In:
    def ejercicio15(self):
        print("If_In")


print("--Cursos--")
print("Matematicas = Biologia = Quimica = Historia ")

curso = input("Ingrese el curso deseado:")

if curso in ("Matematicas",  "Biologia", "Quimica",  "Historia"):
    print("Curso {0} seleccionado.".format(curso))
else:
    print("No existe ese curso...")

