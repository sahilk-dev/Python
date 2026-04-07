# Returns one value
def make_chai():
    return "Here is your masala chai"
    print("Here is your masala chai")

return_value = make_chai()
print(return_value)


# Returns one value
def idle_chaiwala():
    pass

print(idle_chaiwala())

# Returns one value
def sold_cups():
    return 120

total = sold_cups()
print(total)


# Returns early from a function
def chai_status(chai_left):
    if chai_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("Chai")

print(chai_status(0))
print(chai_status(5))


# Returning multiple values
def chai_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = chai_report()
print("Sold: ", sold)
print("Reamining: ", remaining)