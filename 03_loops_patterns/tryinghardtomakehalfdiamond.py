n = 4

# Upper part
for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    for stars in range(2 * i - 1):
        print("*", end="")
    print()

# Down part
for i in range(n - 1, 0, -1):
    for space in range(n - i):
        print(" ", end="")
    for stars in range(2 * i - 1):
        print("*", end="")
    print()
