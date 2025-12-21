import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_csv(r"e:\fake_pubg_20000_matches.csv")
print(df.head())
print(df.tail())
print(df.sample())
print(df.info())
print(df.describe())

# Kills distribution

plt.figure(figsize=(10,5))
plt.hist(df['Kills'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Kills per Match")
plt.xlabel("Kills")
plt.ylabel("Number of Matches")
plt.show()

# damage distribution
plt.figure(figsize=(12,15))
plt.hist(df['Damage'],bins=20, colour= 'valvet', edgecolor= 'black')
plt.title("Damage done per match")
plt.xlabel("damage")
plt.ylabel("Matches")
plt.show()