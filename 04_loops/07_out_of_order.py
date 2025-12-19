# Break, Continue and Loop Fallback

flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")

print(f"Out side of loop")


staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")