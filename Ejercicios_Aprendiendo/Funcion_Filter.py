def filtro(elem):
    return (elem=="o")


l = [1,-3,2,-7,-8,-9,10]
s = "Hola mundo"
lr = list(filter(filtro,s))
print(s)
print(lr)
print(type(lr))#devuelve una lista