#recibe una funcion y emtrega una funcion

loggeado = True

usuario = "Codigofacilito"

def admin(f):
    def comprobar(*args,**kwargs):
        if loggeado:
            f(*args,**kwargs)
        else:
            print("No tiene permiso de ejecutar",f.__name__)
    return comprobar

def decorador(funcion):
    def funciondecorada(*args,**kwargs):#permite recibir n cantidad de atibutos
        print("funcion ejecutada",funcion.__name__)
        funcion(*args,**kwargs)

    return funciondecorada

@admin
@decorador
def resta(n,m):
    print(n-m)

#decorado

resta(3,5)
"""resta(5,3)
decorada = decorador(resta)
decorada(3,5)"""

