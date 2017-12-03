#los generadores no regresan una lista
l = [1,2,3,-1,4]
s = ["H","o","l","a"]

#l2 = [num for num in l if num > 0]

#l2 = (c*num for c in s for num in l if num > 0)

def factorial(n):
    i = 1;
    while (n>1):
        i = n*i
        yield i
        n -= 1
print(l)

##for letra in l2:
##    print(letra)
for e in factorial(5):
    print(e)