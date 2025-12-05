# Take a three-digit number, extract digits, and add their squares

num = int(input("Enter a three-digit number: "))

# Extract digits
a = num // 100          # hundreds digit
b = (num // 10) % 10    # tens digit
c = num % 10            # ones digit

result = a*a + b*b + c*c

print("Sum of squares of digits =", result)
