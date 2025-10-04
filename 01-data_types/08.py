ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")

# Lists in Python are mutable, meaning their contents can be changed after they are created.
# When we modify a list (e.g., by adding or removing elements), the list object remains the same in memory,
# and its id does not change. This is because lists are designed to be dynamic and can grow or shrink as needed.
# In contrast, immutable types like strings or tuples cannot be changed after they are created.
# When we perform operations that would modify these immutable types, a new object is created in memory,
# and the original object remains unchanged.
# The bytearray type is a mutable sequence of bytes, allowing for in-place modifications.
# In the example above, we created a bytearray from a bytes literal and then modified its contents using the replace method.
# This demonstrates the mutable nature of bytearrays, as we were able to change the data without creating a new object.
# The replace method of bytearray works similarly to that of strings, allowing us to replace occurrences of a specified byte sequence with another byte sequence.
# Overall, lists and bytearrays provide flexibility for managing collections of items that may need to change over time, while immutable types like strings and tuples are useful for fixed collections of data that should not be altered. 
# This mutability characteristic is important to understand when working with different data types in Python, as it affects how data is managed and manipulated in memory.
# The concatenation operator (+) creates a new list by combining two existing lists, while the multiplication operator (*) creates a new list by repeating the elements of an existing list a specified number of times.