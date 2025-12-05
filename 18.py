# Check if a number is an Armstrong number

num = int(input("Enter a number: "))
s = str(num)
n = len(s)

total = 0
for digit in s:
    total += int(digit) ** n

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
