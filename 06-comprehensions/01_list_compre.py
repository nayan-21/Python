menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)

# Output: ['Iced Lemon Tea', 'Iced Peach Tea'] 
# This is a list comprehension that filters the menu for items containing "Iced"    
# List comprehensions provide a concise way to create lists based on existing lists.
# They consist of brackets containing an expression followed by a for clause,
# and can include optional if clauses to filter items.
# The general syntax is: [expression for item in iterable if condition]
# They are often more readable and faster than traditional loops for creating lists.
# Example: Creating a list of squares of even numbers from 0 to 9
# squares_of_even = [x**2 for x in range(10) if x % 2 == 0] 