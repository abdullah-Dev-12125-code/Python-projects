import numpy as np
import pandas as pd

Hours= list(range(1,25))
sensors = [f"Sensor {i+1}:"for i in range(5)]

array = np.random.randint(5,20,size=(3,5,24))
days1 = array[0]
days2 = array[1]
days3 = array[2]

df1 = pd.DataFrame(days1,index=sensors,columns=Hours)
df2 = pd.DataFrame(days2,index=sensors,columns=Hours)
df3 = pd.DataFrame(days3,index=sensors,columns=Hours)

print("="*70)
print("\t\t\tLIGHT INTENSITY READINGS")
print("="*70)

print("\n" + "-"*60)
print("\t\t\tDAY 1")
print("-"*60)
print(df1)

print("\n" + "-"*60)
print("\t\t\tDAY 2")
print("-"*60)
print(df2)

print("\n" + "-"*60)
print("\t\t\tDAY 3")
print("-"*60)
print(df3)

print("\n" + "="*70)
