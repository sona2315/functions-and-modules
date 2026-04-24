# Exception handling in Python is used to manage runtime errors (exceptions)
# so that your program doesn’t crash unexpectedly. It lets you gracefully handle errors 
# and continue execution.

# #basic syntax
# try:
#     # code that may raise an exception
#     x = int(input("Enter a number: "))
# except:
#     # runs if an exception occurs
#     print("Invalid input!")
# #__________________________________________________________________
# try:
#     x = int("abc")
# except ValueError:
#     print("Conversion failed!")

#__________________________________________________________________
# Raising exceptions in Python isn’t just about stopping a program—it’s about clearly 
# signaling that something has gone wrong and should not be ignored.

# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Insufficient balance")
# withdraw(2, 14)

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    else:
        print(balance-amount)
    return balance - amount
    

try:
    withdraw(20, 14)
except ValueError as e:
    print("Error:", e)

withdraw(40,5)