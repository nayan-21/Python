chai_type = "Ginger chai"
customer_name = "Nayan"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")

# Strings in Python are sequences of characters, which can include letters, digits, symbols, and whitespace.
# They are immutable, meaning that once a string is created, it cannot be changed.
# Strings can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Triple quotes are often used for multi-line strings or docstrings.
# Python supports various string operations, such as concatenation, slicing, and formatting.
# In the example above, we demonstrate string slicing to extract specific parts of a string.
# We also show how to encode a string into bytes using UTF-8 encoding and then decode it back to a string.
# Encoding is important for handling special characters and ensuring that text is correctly represented in different systems.
# The f-string (formatted string literal) is a way to embed expressions inside string literals, using curly braces {}.
# This allows for more readable and concise string formatting compared to older methods like %-formatting or str.format().
# The slicing operation [start:end] extracts a substring from the original string, where 'start' is the index of the first character to include,
# and 'end' is the index of the first character to exclude. Negative indices can be used to count from the end of the string.
# The slicing operation [::-1] reverses the string by specifying a step of -1.
# This is a common technique to reverse a string in Python.