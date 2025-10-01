is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")
# In Python, the boolean values True and False can be treated as integers in arithmetic operations,
# where True is equivalent to 1 and False is equivalent to 0.
# This allows for operations like addition and multiplication to be performed with boolean values.
# In the example above, adding an integer (stri_count) to a boolean (is_boiling) results in an integer,
# because the boolean is upcast to an integer during the operation.
# Similarly, when checking the presence of milk using an integer (milk_present),
# the integer 0 is interpreted as False when converted to a boolean.
# The logical AND operation (and) between two boolean values (water_hot and tea_added)
# results in another boolean value, which can be used in conditional statements or further logical operations.
# This behavior is a part of Python's dynamic typing and its treatment of boolean values as a subclass of integers.