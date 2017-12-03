#programacion funcional, funciones de orden superior

"""def prueba(f):
    return f()

def porenviar():
    return (2+2)
print(prueba(porenviar))"""

def seleccion(operacion):
    def suma(n,m):
        return n+m
    def multiplicacion(n,m):
        return n*m
    if operacion == "suma":
        return suma
    elif operacion == "multiplicacion":
        return multiplicacion


fguardada = seleccion("suma")

print(fguardada(3,4))

