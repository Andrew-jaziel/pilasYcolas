"""1. Atención a los pacientes de un consultorio médico.

a. Escribir una clase ColaDePaciente, con los métodos nuevoPaciente,
que reciba los nombre y apellidos del paciente y lo encole; un
método llamado pacienteActual que devuelva el primer paciente en
la cola y lo desencole.
b. Escribir un programa que permita al usuario ingresar nuevos
pacientes, ver pacientes que esperan e imprimir el paciente que se va
atender."""

class Paciente: 
    #Paciente
    def __init__(self,nom, ape):
     
     
     self.nombres = nom
     self.apellidos  = ape 
     
     
    def __str__(self):
        return f"""Nombres: {self.nombres}
Apellidos: {self.apellidos}"""

class Cola:
    def __init__(self):
        self.elementos = []

    def pacienteNuevo(self, elem):
        self.elementos.append(elem)

    def quitar(self):
        try:
           return self.elementos.pop(0)
        except Exception as ex:
           print("Cola vacía...", str(ex))

    def estaVacia(self):
        return self.elementos == []