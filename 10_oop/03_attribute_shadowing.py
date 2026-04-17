class Chai:
    tempreture = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.tempreture)

cutting.tempreture = "Mild"
cutting.cup = "small"
print("After changing ", cutting.tempreture)
print("cup size is ", cutting.cup)
print("Direct look into the class ", Chai.tempreture)

del cutting.tempreture
del cutting.cup
print(cutting.tempreture)
print(cutting.cup)