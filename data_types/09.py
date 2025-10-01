essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")

# Sets are unordered collections of unique elements in Python.
# They are defined by enclosing elements in curly braces {} or by using the set() constructor.
# Sets automatically handle duplicate values by storing only one instance of each unique element.
# Common set operations include union (|), intersection (&), and difference (-).
# The union operation combines elements from both sets, the intersection operation finds common elements, 
# and the difference operation finds elements that are in one set but not the other.
# Membership testing can be performed using the 'in' keyword to check if an element exists within the set.
# This is useful for validating the presence of an item in a collection.
# Sets are mutable, meaning that elements can be added or removed after the set is created.
# However, the elements themselves must be immutable types (like strings, numbers, or tuples).
# Sets are often used for operations involving uniqueness, membership testing, and mathematical set operations.
# They are particularly useful in scenarios where the order of elements is not important, and duplicates need to be eliminated.
# Note that sets do not support indexing or slicing since they are unordered collections.