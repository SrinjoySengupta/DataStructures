# Program to find LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find HCF using Euclid's algorithm
x, y = a, b
while y != 0:
    x, y = y, x % y
hcf = x

lcm = (a * b) // hcf

print("LCM =", lcm)
