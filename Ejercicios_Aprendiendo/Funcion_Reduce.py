#reducir una secuencia a un solo elemento
import functools

s = ("H","o","l","a")

def concatenar(a,b):
    return a+b

sr = functools.reduce(concatenar,s)

print(type(sr))
print(sr)