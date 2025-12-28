import numpy as np

cities = [
    "Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta",
    "Multan", "Faisalabad", "Hyderabad", "Sialkot", "Rawalpindi"
]

Temp = np.random.randint(15, 41, size=(10, 7))

Average = np.mean(Temp, axis=1)
HottestDay = np.max(Temp)
ColdestDay = np.min(Temp)

HighestMeanTemp = np.max(Average)
HighestCity = cities[np.argmax(Average)]

print('-'*40)
print("\t\tTemperature Data")

for city, temps in zip(cities, Temp):
    print(city, temps)

print('-'*40)
print("\t\tAverage Temperature")

for city, avg in zip(cities, Average):
    print(f"{city}: {avg:.2f}")

print('-'*40)
print("\t\tHighest Average Temperature")
print(f"{HighestCity}: {HighestMeanTemp:.2f}")

print('-'*40)
print("\t\tHottest Day Temperature")
print(HottestDay)

print('-'*40)
print("\t\tColdest Day Temperature")
print(ColdestDay)
print('-'*40)

