def safe_divisor():
    try:
        x = a/b 
        print(x)
    except ZeroDivisionError:
        print("Error") 
    except ValueError:
        print("provide a number")
    except:
        print("Something went wrong")
    

a = int(input("enter a numinator here: "))
b = int(input("enter a denominator here: "))
c = safe_divisor()
if c is not None:
    print(f"The division of {a} and {b} is {c} ")
    
