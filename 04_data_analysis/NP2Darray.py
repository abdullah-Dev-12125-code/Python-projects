import numpy as np

array = np.random.randint(10,40,size=(5,10))
shape = np.shape(array)
size  = np.size(array) 

print("-"*50)
print("\t\t Array")
print(array)
print("-"*50)
print("\t\tSize")
print(size)
print("-"*50)
print("\t\tShape")
print(shape)
