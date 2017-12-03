class Humano:
    def __init__(self,edad):
        self.edad = edad


    def hablar(self,mensaje):
        print(mensaje)


class IngSistemas(Humano):
    def __init__(self): ##tiene mayor importancia que el init de la superclase
        print("Holaaa")
    def programar(self,lenguaje):
        print("Voy a programar en ",lenguaje)

class LicDerecho(Humano):
    def __init__(self,escuela):
        print("Lic en Derech egresado de: ",escuela)
    def estudiarCaso(self,de):
        print("Debo estudiar el caso de ",de)

class estudioso(LicDerecho,IngSistemas):##pass
    pass # es como un vete, no hay nada que ver aqui, es como no hay ningun método


pepe = estudioso("UAN")
pepe.hablar("Hola soy de herencia multiple")
pepe.programar("C++")
pepe.estudiarCaso("Juan")

