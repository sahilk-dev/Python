# Set and frozenset

essential_spices = {"cardamom", "ginger", "cinnamom"}
optional_spices = {"cloves", "ginger", "black pepper"}

# | -> Pipe operator or Union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# & -> Intersection or Common
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# Differences
only_in_essentials = essential_spices - optional_spices
print(f"only_in_essentials spices: {only_in_essentials}")

# membership test
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

# Frozen set
mylist = ["X", "Y", "Z"]
print(mylist)
x = frozenset(mylist)
x[2] = "A"
print(x)