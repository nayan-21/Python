tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)

# Dictionary comprehensions provide a concise way to create dictionaries based on existing iterables.
# They consist of curly braces containing a key-value pair expression followed by a for clause,
# and can include optional if clauses to filter items.
# The general syntax is: {key_expression: value_expression for item in iterable if condition}
# They are often more readable and faster than traditional loops for creating dictionaries.
# Example: Creating a dictionary of squares of even numbers from 0 to 9
# squares_of_even = {x: x**2 for x in range(10) if x % 2 == 0}
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
