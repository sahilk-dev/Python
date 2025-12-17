# Task 3:
    # * Input: "small", "medium", "large"
    # * Small-> $10, Medium-> $15, Large-> $20
    # * If invalid: show "Unknown cup size"

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is $10")
elif cup == "medium":
    print("Price is $15")
elif cup == "large":
    print("Price is $20")
else:
    print("Unknown cup size")