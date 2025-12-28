
def momentum(kg,vel):
    Calculation = kg * vel
    return Calculation


while True:
    try:
        Mass = int(input("Enter mass of object(kg): "))
        Velocity= int(input("Enter velocity of object(m/s): "))
        break    
    except ValueError:
        print("Accepts Numeric values only!!")

CAl = momentum(Mass,Velocity)

print("momentum:",CAl,'N-s')