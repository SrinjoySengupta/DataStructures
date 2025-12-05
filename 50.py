# Program to simplify a fraction

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

# Find GCD (Greatest Common Divisor)
a, b = num, den
while b != 0:
    a, b = b, a % b
gcd = a

# Simplified fraction
simple_num = num // gcd
simple_den = den // gcd

print("Simplified fraction:", simple_num, "/", simple_den)
