sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# when changing the value of sugar_amount from 2 to 12,
# a new integer object is created in memory for 12,
# and sugar_amount now references this new object.
# The original integer object 2 remains unchanged in memory.
# This is because integers are immutable in Python.