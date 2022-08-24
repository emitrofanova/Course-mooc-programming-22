# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

print("The roots are", (-b + sqrt(b**2 - 4*a*c))/(2*a), "and", (-b - sqrt(b**2 - 4*a*c))/(2*a))

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5