"""def decorador(funcion):
    def funciondecoradora(*args,**kwargs):
        print("Funcion ejecutada ",funcion.__name__)
        funcion(*args,**kwargs)

    return funciondecoradora"""
class decorador(object):
    """Mi clase decoradora"""
    def __init__(self,funcion):
        self.funcion = funcion
    def __call__(self, *args, **kwargs):
        print("Funcuon ejecutada",self.funcion.__name__)
        self.funcion(*args,**kwargs)


@decorador
def resta(n,m):
    print(n-m)

resta(3,5)