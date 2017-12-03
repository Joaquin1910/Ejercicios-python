# es un fragmento de codigo en el cual hacemos una tarea, les podemos enviar unos parametros
#hacemos el proceso con el y enviamos la salida

def mi_funcion(num1,num2):
    print(num1 + num2)

x = float(input("Ingrese el primer numero: "))
y = float(input("Ingrese el primer numero: "))
mi_funcion(x,y)


def mi_funcion(caden,v=2):
    print(caden*v)

mi_funcion("Joaquin",10)

def mi_funcion(caden,v,*algomas):
    print(caden*v)
    for cadena in algomas: #en algo mas se va a guardar en forma de tupla
        print(cadena*v)

mi_funcion("Joaquin",5,"Hola","sapo")

def mi_funcion(caden,v,**algomas):#en algo mas se va a crear un diccionario
    print(caden*v)

    print(algomas['cadenaextra'])
    print(algomas['cadenamas'])

mi_funcion("Joaquin",5,cadenaextra = "Hola",cadenamas ="Adios")

def mi_funcion (num1,num2):
    return num1+num2

resultado_de_suma = mi_funcion(3,4)
print(resultado_de_suma)