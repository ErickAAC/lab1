import math

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

gcd = math.gcd(x, y)

print(f"The GCD of {x} and {y} is {gcd}")