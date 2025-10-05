favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

print(favourite_chais)
chai_set = set(favourite_chais)
print(chai_set)


unique_chai = {chai for chai in favourite_chais }
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)

# Set comprehensions provide a concise way to create sets based on existing iterables.
# They consist of curly braces containing an expression followed by a for clause,  
# and can include optional if clauses to filter items.
# The general syntax is: {expression for item in iterable if condition} 
# They are often more readable and faster than traditional loops for creating sets.
# Example: Creating a set of unique characters from a string
# unique_chars = {char for char in "chaicode" if char not in "aeiou"}
# Output: {'c', 'd', 'h', 'i', 'o', 'a', 'e'}
