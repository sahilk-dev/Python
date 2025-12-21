# Easy Level- Daily Expense Tracker

expenses = [500, 250, 800, 40, 90]
total = 0

total = sum(expenses) # This is the one line shortcut instead of using for loop or Optimized way.

for expense in expenses:
    total += expense
    
print(f"Total expense for the day is: ${total}")


# Password Length Checker

password = input("Enter the Password: ")
minimum_length = 8

if len(password) >= minimum_length:
    print("Password is vaild!")
elif len(password) < minimum_length:
    print(f"Password is Invalid. Must be at least {minimum_length} characters.")