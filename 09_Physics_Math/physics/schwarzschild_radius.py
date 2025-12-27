G = 6.674e-11
c = 3e8
M_sun = 1.989e30

num_suns = int(input("Enter number of Suns: "))
M = num_suns * M_sun

rs = 2 * G * M / c**2
print(f"Schwarzschild Radius: {rs} meters")
print(f"In kilometers: {rs / 1000} km")
