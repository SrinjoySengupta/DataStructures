# Reverse a four-digit number and check if the reverse is same

num = int(input("Enter a four-digit number: "))

# Reverse the number
rev = int(str(num)[::-1])

print("Reversed number:", rev)

# Check if reverse is same
if num == rev:
    print("Reverse is true (It is a palindrome)")
else:
    print("Reverse is false (Not a palindrome)")
