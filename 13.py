# Check if a number is divisible by 3, 6, both, or neither

num = int(input("Enter a number: "))

if num % 6 == 0:
    print("Divisible by both 3 and 6")
elif num % 3 == 0:
    print("Divisible by 3 only")
else:
    print("Not divisible by 3 or 6")
