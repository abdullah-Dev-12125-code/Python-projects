def conversion(choice, value):
    if choice == 'F to C':
        C = (value - 32) * 5/9
        return C
    elif choice == 'C to F':
        F = (9/5 * value) + 32
        return F

choice = input("Enter conversion type (F to C or C to F): ")

if choice == 'F to C':
    F = float(input("Enter the temperature in Fahrenheit: "))
    print("Temperature in Celsius:", conversion(choice, F))

elif choice == 'C to F':
    C = float(input("Enter the temperature in Celsius: "))
    print("Temperature in Fahrenheit:", conversion(choice, C))

else:
    print("Invalid choice. Please enter 'F to C' or 'C to F'.")
