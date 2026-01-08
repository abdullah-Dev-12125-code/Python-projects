tuple1 = (1,2,3) 
tuple2 = ('A','B','C')
tuple3 = tuple1 + tuple2

print("Concatinated Tuple",tuple3)
print("\nTuple type ")
print(f"--{type(tuple3)}--")

num ,*alpha = tuple3 
print("Num",num,":","Alpha",alpha)

print("Num",num)
print("Alpha",alpha)

try:
    list_list = [1,2,3,4,5,6]
    tuple_tuple = (1,2,3)
    list_tuple = list_list + tuple_tuple 
except Exception as e:
    print("You can concate a list in tuple!!")
    