chai = "Ginger chai"

def prepare_chai(order):
    print("Preparing", order)



prepare_chai(chai)
print(chai)


chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 43

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # Positional Arguments
make_chai(tea="Green", sugar="Medium", milk="No") # Keywords



def special_chai(*ingridents, **extras): # *ingridents -> *args || ** extras -> **kwargs
    print("Ingridents", ingridents)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="yes")


# Default
def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()
chai_order()

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()