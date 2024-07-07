naresh={1,3,4,2,5,6}
print(type(naresh))
naresh.add(8)
print(naresh)
naresh.update({9,7,6,54})
print(naresh)
naresh.remove(1)
print(naresh)
naresh.pop()
print(naresh)
naresh.clear()
print(naresh)
a=naresh.copy()
print(a)

set1={1,2,3,4}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.isdisjoint(set2))

set3={1,2,3,4,5,6,7,8}
set4={1,2,3,4}
print(set3.issuperset(set4))
print(set4.issubset(set3))
print(set3.issubset(set4))
print(set4.issuperset(set3))

for i in {1,2,3,4,5}:
    if i==2:
        print("hai")
    else:
        print("bye")

a=[1,2,3,4]
b=frozenset(a)
print(b)
