lista = [1,"Dos",3]

#buscar = 0
##buscar = float(input())
""""print (buscar in lista)#buscar osea 1 esta en lista?

print(lista.index(buscar))#obtener la posicion de 1

if buscar in lista:
    print("El elemento esta y su posicion es ",lista.index(buscar))


else:
    print("El elemento no se encuentra")"""

#agregar un elemento a la lista
print(lista)
lista.append("Nuevo elemento")
print(lista)
print(lista.count(3))#cuenta la cantidad
print(lista)
lista.insert(2,"Nuevo")#agrega la posicion 2 a Nuevo
iterable = "cadena"
print(lista)
#lista.extend(iterable)#extiende la lista de una a otra, no devuelve una lista nueva, sino la tranforma
print(lista.pop())#saca el ultimo elemento de la lista y lo borra
print(lista)
print(lista.pop(2))#extrae y borra el elemento en la posicion dos
print(lista)

lista.remove(3)#elimina el 3
print(lista)
#invertir los elementos de la lista
lista.reverse()
print(lista)



