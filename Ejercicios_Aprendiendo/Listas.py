l = [2,"tres",True,["uno",10]]
print(l)

l2 = l[1] #acceder a un elemento de la lista
print(l2)

l3 = l[3][0] #acceder al elemento de una lista que esta dentro de otra lista
print(l3)

l[0]=4 #cambiar valor de un elemento
print(l[0])

l3 = l[0:3]#Tomar 3 elementos de la lisla
print(l3)

l5 =l[0:3:2] #extraer elementos escalados
print(l5)

l7 = l[0::2] #tomar todos los elementos escalados de 2 en 2
print(l7)

l[0:2] = [4,3] #cambia los dos primeros elementos
print(l)

l2 = l[-1] #imprime el orden inverso
print(l2)

