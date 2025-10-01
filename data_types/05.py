import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
print(sys.float_info)

# Floating point numbers are represented in computer hardware as base 2 (binary) fractions.
# This can lead to small rounding errors in calculations, as some decimal fractions cannot be represented exactly   
# in binary. For example, 0.1 in decimal is a repeating binary fraction.
# This is why operations like subtraction can yield results that are very close to, but not exactly, the expected value.
# The sys.float_info provides details about the precision and limits of floating point numbers in Python.
# For applications requiring high precision, such as financial calculations, consider using the Decimal or Fraction classes from Python's standard library.
# The Decimal class provides decimal floating point arithmetic with more precision and control over rounding.
# The Fraction class provides support for rational number arithmetic.
# These classes can help mitigate issues related to floating point precision.