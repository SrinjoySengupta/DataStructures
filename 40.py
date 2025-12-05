# Program to reverse a number manually (without string)

num = int(input("Enter a number: "))
n = abs(num)
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

# restore sign if negative
if num < 0:
    rev = -rev

print("Reversed Number:", rev)
