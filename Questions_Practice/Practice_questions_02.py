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


# Attendance Counter

attendance = ["P", "A", "P"]
present_count = 0

for attend in attendance:
    if attend == "P":
        present_count += 1

print(f"The total number of students presents are: {present_count}")


# Online Shopping Discount

total_amount = 6001

if total_amount >= 5000:
    discount = 20
elif total_amount >= 2000:
    discount = 10
else:
    discount = 0

discount_amount = (total_amount % discount) / 100
final_price = total_amount - discount_amount

print(f"You got a discount of {discount}%")
print(f"The final price after a {discount}% discount is: ${final_price}")