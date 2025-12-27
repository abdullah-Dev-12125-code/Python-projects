import numpy as np

N = int(input("Enter a number here: "))

for i in range(1,N+1):
    if i % 2== 0:
        print(i,"Is Even")
    else:
        print(i,"Is Odd")

Matrix1 = np.array([[1,  2,  3],
                    [2,  5,  6],
                    [7, -1,  2],])


Matrix2 = np.array([[3,  2, -8],
                    [2,  7, -7],
                    [7, -1,  2],])




Sums = Matrix1 + Matrix2
product = Matrix1 @ Matrix2
diffrence = Matrix1 - Matrix2


print("Sum:", Sums)
print("product", product)
print("diffrence", diffrence)


# Speed
Time = float(input("Enter Time in Seconds: "))
Distance = float(input("Enter speed in meters: "))

v = Distance/Time
print("Speed(M/S) =",v)
print("Speed(Km/h)=",v * 3.6)


# Acceleration
final_Velocity = int(input("Enter Vf here: "))
Initial_Velocity = int(input("Enter Vi here: "))
Times = float(input("Enter Time in seconds: "))

Acceleration = final_Velocity - Initial_Velocity / Times
print("Acceleration",Acceleration)


# Force
mass = float(input("Enter mass (kg): "))
acceleration = float(input("Enter acceleration (m/s^2): "))

force = mass * acceleration
print("Force is", force, "Newtons")


# Mass 
force = float(input("Enter force (N): "))
acceleration = float(input("Enter acceleration (m/s^2): "))

mass = force / acceleration
print("Mass is", mass, "kg")


# Weight Calculator
mass = float(input("Enter mass (kg): "))
g = 9.8  # gravity

weight = mass * g
print("Weight is", weight, "Newtons")


# Distance Calculator
vi = float(input("Enter initial velocity (m/s): "))
time = float(input("Enter time (s): "))
a = float(input("Enter acceleration (m/s^2): "))

distance = vi * time + 0.5 * a * time**2
print("Distance travelled is", distance, "meters")


# Time Calculator
distance = float(input("Enter distance (meters): "))
velocity = float(input("Enter velocity (m/s): "))

time = distance / velocity
print("Time taken is", time, "seconds")


# Kinetic Energy Calculator
mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))

KE = 0.5 * mass * velocity**2
print("Kinetic Energy is", KE, "Joules")


# Potential Energy Calculator
mass = float(input("Enter mass (kg): "))
height = float(input("Enter height (meters): "))
g = 9.8

PE = mass * g * height
print("Potential Energy is", PE, "Joules")


# Work Calculator
force = float(input("Enter force (Newtons): "))
distance = float(input("Enter distance (meters): "))

work = force * distance
print("Work done is", work, "Joules")


