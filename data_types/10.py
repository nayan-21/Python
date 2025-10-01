chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")

# Dictionaries in Python are mutable collections of key-value pairs.
# They are defined by enclosing elements in curly braces {} and consist of keys and values separated by colons (:).
# Keys must be unique and immutable types (like strings, numbers, or tuples), while values can be of any data type and can be duplicated.
# Dictionaries support various operations, including adding, updating, and removing key-value pairs.
# The popitem() method removes and returns the last inserted key-value pair as a tuple.
# The update() method allows merging another dictionary or iterable of key-value pairs into the existing dictionary.
# Membership testing can be performed using the 'in' keyword to check if a key exists within the dictionary.
# This is useful for validating the presence of an item in a collection.
# The get() method retrieves the value for a specified key, returning a default value if the key is not found.
# This prevents KeyError exceptions and allows for safer access to dictionary values.
# Dictionaries are often used for storing and managing related data, such as configurations, settings, or any scenario where a mapping between keys and values is needed.
# They provide efficient lookups and are widely used in various applications, including web development, data processing, and more. 