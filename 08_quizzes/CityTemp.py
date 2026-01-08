import numpy as np

# 10 rows, 7 columns, random temperatures between 25 and 50
temperature_random = 25 + (50 - 25) * np.random.rand(10, 7)

# Convert to integers
temperature_random_int = temperature_random.astype(int)

print("Random Temperature Array (10x7) as Integers:")
print(temperature_random_int)

# Average temperature of all data
avg_temp = np.mean(temperature_random_int)
print("\nAverage Temperature Overall:", avg_temp)

# Average temperature of each city (column-wise)
avg_temp_per_city = np.mean(temperature_random_int, axis=0)
print("\nAverage Temperature of Each City:")
for i, temp in enumerate(avg_temp_per_city, start=1):
    print(f"City {i}: {temp:.2f}")
