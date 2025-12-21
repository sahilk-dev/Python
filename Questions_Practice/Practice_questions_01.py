# Easy

students = ["Rahul", "Anita", "Sahil", "Neha"]

for name in students:
    # print("Present:", name)
    pass


names = ["X", "Y", "Z", "A"]
prices = [40, 60, 120, 30]

for name, amount in zip(names, prices):
    # print(f"The Price of {name} is: {amount} rupees.")
    pass

# Medium

prices = [250, 120, 80, 50]
total = 0

for price in prices:
    total += price

# print("Total bill:", total)


password = "Sahil123"
has_digit = False

for char in password:
    if char.isdigit():
        has_digit = True

# print("Contains number:", has_digit)

# Hard

marks = [78, 45, 60, 30, 90]
total = 0
pass_count = 0

for mark in marks:
    total += mark
    if mark >= 40:
        pass_count += 1

average = total / len(marks)

# print("Average marks:", average)
# print("Students passed:", pass_count)


expenses = [12000, 15000, 18000, 9000, 20000]
limit = 15000

for month, amount in enumerate(expenses, start=1):
    if amount > limit:
        # print(f"Month {month}: Over budget ({amount})")
        pass


from datetime import datetime

orders = [
    {"id": 1, "status": "delivered"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "cancelled"},
]

for order in orders:
    if order["status"] == "pending":
        print("Processing order ID:", order["id"])
    elif order["status"] == "delivered":
        delivered_time = datetime.now().strftime("%d %B %Y, %I:%M %p")
        print(f"Your item has been delivered on {delivered_time} having order ID:", order["id"])
    elif order["status"] == "cancelled":
        print("Your order has been cancelled!")
    else:
        print("Invalid order ID")