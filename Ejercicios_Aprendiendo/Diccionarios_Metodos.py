"""def is_cool(name):
    return (name == "I")

def person(name):
    if is_cool(name):
        print(name," Is Cool")
    else:
        print(name, "You are Cool")

person("I")
person("You")"""

diccionario = {
    "redes_sociales": ["Twiter","Facebook","Linkedin"],
    3: "tres",
    "Hola": "Mundo"
}
#comprobar si tiene o nod clave
print("Hola" in diccionario)

#devuelve una lista, donde cada elemento de la lista es una tupla, entrega el key y sus ele
print(diccionario.items())

#devuelve una lista unicamente con las claves
print(diccionario.keys())
#devuelve la lista con los valores del diccionario
print(diccionario.values())
#devuelve el valor del elemento que borramos, elimina la clave y el elemnt
##print(diccionario)
##print(diccionario.pop())
print(diccionario)
#para eliminar unicamente un elemento de un diccionario
del diccionario["Hola"]
print(diccionario)
#borrar todos los elemenos del diccionario
#diccionario.clear()
#print(diccionario)
#diccionario["clave nueva"]="valor"
#print(diccionario)
#crear una copia del diccionario
diccionario_2 = diccionario.copy()
print(diccionario)
print(diccionario_2)