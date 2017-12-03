#funcion a utilizar con map y reduce


#def suma(n,m):
#    return n+m

#funcion a utilizar con filter
#def filtrar(n):
#    return (n == "o")


import functools
li = [1,-2,1,-4]
lo = [5,3,6,7]
s = "Hola mundo"

suma = lambda n,m:n+m

print(list(map(suma,li,lo)))
print(list(filter(lambda n: n == "o",s)))
print(functools.reduce(lambda n,m:n+m,lo))

print(suma(5,4))