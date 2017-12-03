#atributo son las caracteristicad del objeto y metodo son las acciones del objeto

class Humano:
    def __init__(self,edad):
        self.edad = edad


    def hablar(self,mensaje):
        print(mensaje)

pedro = Humano(26)
raul = Humano(21)


pedro.hablar("Hola")
raul.hablar("Hola soy pedro")

print("Soy pedro y tengo ",pedro.edad)
print("Soy raul y tengo ",raul.edad)

