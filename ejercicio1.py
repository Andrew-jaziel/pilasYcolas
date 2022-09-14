class Libro:
    def __init__(self, tit, aut, edi):
        self.titulo = tit
        self.autor = aut
        self.edicion = edi

    def __str__(self):
        return f"""Titulo: {self.titulo}
Autor: {self.autor}
Edición: {self.edicion}"""


pila = []


def menu():
    print("Pila")
    print("1. Libros a tomar prestados ")
    print("2. Mostrar libros a sacar de la biblioteca")
    print("3. Salir")
    print("Digite la opcion")


def librosAtomar():
    tit = input("Titulo del libro a tomar: ")
    aut = input("Autor del libro: ")
    edi = int(input("Edición del libro: "))
    pila.append(Libro(tit, aut, edi))
    print("Libro apilado...")
   

def mostrarPila():
    
    for libro in pila:
        print("Libro que lleva el lector: ")
        print(libro)
        print("recuerde que es de caracter devolutivo....")

    
    
 


def principal():
    try:
        op = 0
        while (op != 4):
            menu()
            op = int(input())
            if (op == 1):
                librosAtomar()
            elif (op == 2):
                mostrarPila()
            elif (op == 3):
                print("Adios")
            else:
                print("Opcion invalida....")

    except Exception as ex:
        print("Error:", str(ex))


principal()