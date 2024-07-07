#n=(1,6,2,4,3)
#print(type(n))
#print(n[0:4:2])

#print(min(n))
#print(max(n))
#print(len(n))
#print(sum(n))

a=(1,2,3)
b=(4,5,6)
#print(a+b)
n=[]
for i,j in zip(a,b):
    n.append(a+b)

print(tuple(n))

print(1 in a)
print(2 not in b)
print(a is b)
print(a is not b)
    