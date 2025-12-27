import math

t0 = 1
c = 300_000_000   # speed of light in m/s
v = 0.99 * c      # convert fraction to m/s

tD = t0 / math.sqrt(1 - (v**2 / c**2))

print("Dilated time:", tD, "seconds")

