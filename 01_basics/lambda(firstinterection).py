import math
square = lambda x: x*x
cube = lambda x: x*x*x
average = lambda x,y,z: (x+y+z)/3


print(average(4,5,6))
print(square(10))
print(cube(10))

lists = [1,2,34,5,56,7,745,45,453,233,552,534,788,32]
nlists = []
for i in lists:
    nlists.append(cube(i))
print(nlists)

m = list(map(cube,lists))

newl = list
print(m)

