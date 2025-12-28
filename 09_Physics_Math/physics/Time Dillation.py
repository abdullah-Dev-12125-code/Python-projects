import math

t0 = 1
c = 300_000_000   
v = 0.99 * c      

tD = t0 / math.sqrt(1 - (v**2 / c**2))

print("Dilated time:", tD, "seconds")

