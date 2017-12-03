#iteraciondes de orden superior,

def op(n,m):
    if n == None or m == None:
        return 0

    return n+m

l = [1,2,3,4]
t = (9,8,7,6)

lr = list(map(op,l,t))#le envia a operador cada uno de los elementos de la lista y tupla

print(l)
print(t)
print(lr)

s1 = "Hola"
s2 = "Mundo"
lr = list(map(op,s1,s2))
print(lr)
