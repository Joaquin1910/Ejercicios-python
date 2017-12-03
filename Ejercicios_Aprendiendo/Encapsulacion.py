#los atributos y alginod metodos tienen la prpiedad de ser privados o publicos
"""class Prueba(object):
    def __init__(self):
        self.__privado = "soy privado"
        self.privado = "soy publico"

    def __metodoPrivado(self):
        print("Soy privado")

    def metodopublico(self):
        print("Soy publico")

    def getPrivado(self):
        return self.__privado

    def setPrivado(self,valor):
        self.__privado = valor

obj = Prueba()

#print(obj.privado)
#print(obj.__privado)
##obj.metodopublico()
##obj.__metodoPrivado()
obj.setPrivado("Tengo un nuevo valor")
print(obj.getPrivado())"""

class Prueba(object):
    def __init__(self):
        self.__privado = "soy privado"
        self.privado = "soy publico"

    def __metodoPrivado(self):
        return ("Soy privado")

    def metodopublico(self):
        print("Soy publico")

    def getPrivado(self):
        return self.__privado

    def setPrivado(self,valor):
        self.__privado = self.__metodoPrivado()

obj = Prueba()


obj.setPrivado("Tengo un nuevo valor")
print(obj.getPrivado())