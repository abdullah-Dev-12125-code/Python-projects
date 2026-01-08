balance = 5000

def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient budget")
    balance-=amount
    return balance
try:
    current_balance = 500
    withdraw_amount = 600
    new_balance=withdraw(current_balance,withdraw_amount)
    print(f"Withdrawal is succesfull Remaining balance: {withdraw}")
except Exception as e:
    print(e)
    


