import pandas as pd
import matplotlib.pyplot as plt

Data = [25000, 30000, 18000, 22000, 27000, 29000, 31000]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
df = pd.DataFrame(Data, index=days, columns=['Sales'])
print(df)

# Line plot
plt.plot(df.index, df['Sales'], marker='o')
plt.title("Weekly Sales")
plt.xlabel("Day")
plt.ylabel("Sales ($)")
plt.show()

# Bar plot
plt.bar(df.index, df['Sales'], color='skyblue')
plt.title("Weekly Sales")
plt.xlabel("Day")
plt.ylabel("Sales ($)")
plt.show()
    
