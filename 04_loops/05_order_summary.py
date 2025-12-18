# You're preparing an order summary with customer names and total bill.
# Tasks:
    # Use two lists: one for names and one for bills.
    # Print: "[Name] paid [amount]"

# Zip()
names = ["Sahil", "Meera", "Sam", "Alia"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")