daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)

# Generator expressions provide a memory-efficient way to create iterators.
# They consist of parentheses containing an expression followed by a for clause,    
# and can include optional if clauses to filter items.
# The general syntax is: (expression for item in iterable if condition)
# They are often more readable and faster than traditional loops for creating iterators.
# Example: Calculating the sum of squares of even numbers from 0 to 9
# sum_of_squares = sum(x**2 for x in range(10) if x % 2 == 0)
# Output: 220
# Note: Generator expressions do not produce a list; they produce a generator object that generates items on-the-fly.
# This is more memory efficient for large datasets.
# To convert a generator expression to a list, you can use the list() function:
# squares_list = list(x**2 for x in range(10) if x % 2 == 0)
# Output: [0, 4, 16, 36, 64]
# However, using list() negates the memory efficiency advantage of generator expressions.
