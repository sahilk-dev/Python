# Basics of Lists

ingredients = ["water", "milk", "black tea"]

# add
ingredients.append("sugar") #adds the new element to the very end of the list
print(f"Ingredients are: {ingredients}")

# remove
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardmom"]
chai_ingredients = ["water", "milk"]

# Combine both lists
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea") # add the new element at a specific, designated index
print(f"chai: {chai_ingredients}")

# pop: remove the last element
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse() # reverse the list
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

# maximum ands minimum
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Maximum sugar level: {min(sugar_levels)}")

# Operator Overloading and bytearray
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mixed = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mixed}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

# Bytearray
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")