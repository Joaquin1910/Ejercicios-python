#reemplaza en la version 3 a lo que es map y filter

l = [1,2,3,-1,4]
s = ["H","o","l","a"]

l2 = [num for num in l if num>0]

l2 = [c*num for c in s for num in l if num>0]

print(l)
print(l2)
