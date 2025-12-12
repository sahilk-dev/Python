# String - Index, Slice & Encoding

# Core
chai_type = "Ginger chai"
customer_name = "Sahil"

# Formated String
print(f"Order for {customer_name} : {chai_type} please !")

# Slicing, Indexing
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"First word: {chai_description[12:]}")
print(f"First word: {chai_description[::-1]}")

# Encoding - Decoding
label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")