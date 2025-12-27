vi = float(input("Enter initial velocity (m/s): "))
vf = float(input("Enter final velocity (m/s): "))
t = float(input("Enter time (seconds): "))

acceleration = (vf - vi) / t
print("Acceleration =", acceleration, "m/s²")
