# Multiply two numbers without using * operator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = 0

for _ in range(abs(b)):
    result += a

# If second number is negative, make result negative
if b < 0:
    result = -result

print("Product =", result)
