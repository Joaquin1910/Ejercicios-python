#while True: # es una condicion que siempre se va a cumplir, es un bucle infiniro
#    print("Hola")

"""edad = int(input("Ingrese su edad"))

while edad < 20:
    print("Tienes: "+str(edad))
    edad = edad + 1"""


"""edad = int(input("Ingrese su edad")) # si queremos que no imprima el 15

while edad <= 20:
    if edad == 15:
        edad = edad + 1 #para que se imprima hasta el 20 sin mostrar el 15
        continue #No continua, no toma el 15
    print("Tienes: "+str(edad))
    edad = edad + 1"""

"""edad = int(input("Ingrese su edad")) # si queremos que no imprima el 15

while edad <= 20:
    if edad == 15:
        break #rompe el ciclo, solo muestra hasta el 14
    print("Tienes: "+str(edad))
    edad = edad + 1"""
#el for sirve para recorrer las listas, tuplas y diccionarios

lista = ["Elemento 1","Elemento 2","Elemento 3"]
for cosa in lista: #la variable cosa va tomando cada valor de la lista
    print(cosa)

for letra in "Joaquin": #Imprime cada letra de la cadena Joaquin
    print(letra)


