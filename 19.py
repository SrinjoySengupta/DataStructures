# A narcissist number (Armstrong number) is a number that is equal to
# the sum of its own digits each raised to the power of the number of digits.
# Example: 1634 = 1^4 + 6^4 + 3^4 + 4^4

# Program to check if a 4-digit number is a narcissist number

num = int(input("Enter a 4-digit number: "))

s = str(num)
n = len(s)   # should be 4

total = 0
for digit in s:
    total += int(digit) ** n

if total == num:
    print("Narcissist number")
else:
    print("Not a narcissist number")
