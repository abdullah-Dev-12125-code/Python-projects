ticket_ids = ["AVT1215M", "TLR0818E", "HPT1012A"]


Movie_code = []
Seat_Number = []
Ticket_Price = []
Show_time = []




def Movie_code_extraction():
    for Moviecode in ticket_ids:
        Movie_code.append(Moviecode[:3])


def Seat_Number_extraction():
    for seat in ticket_ids:
        Seat_Number.append(seat[3:5])


def Ticket_price_extraction():
    for price in ticket_ids:
        Ticket_Price.append(int(price[5:7]))


def Show_time_extraction():
    for time in ticket_ids:
        Show_time.append(time[7:] )




def total_cost():
    total = sum(Ticket_Price)
    return total
       




Movie_code_extraction()
Seat_Number_extraction()
Ticket_price_extraction()
Show_time_extraction()
total_cost()


print("\nDetails!!\n")
print("For ticket 1 ")
print("Your movie code is",Movie_code[0])
print("Your seat number is",Seat_Number[0])
print(f"Yout ticket price is {Ticket_Price[0]}$")
print("Show time is",Show_time[0])


print("\nDetails!!\n")
print("For ticket 2 ")
print("Your movie code is",Movie_code[1])
print("Your seat number is",Seat_Number[1])
print(f"Yout ticket price is {Ticket_Price[1]}$")
print("Show time is",Show_time[1])


print("\nDetails!!\n")
print("For ticket 3 ")
print("Your movie code is",Movie_code[2])
print("Your seat number is",Seat_Number[2])
print(f"Yout ticket price is {Ticket_Price[2]}$")
print("Show time is",Show_time[2])




print(f"\nYour Total cost is {total_cost()}$\n")
