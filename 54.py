s = input("Enter a string: ")
ch = input("Enter the character to find: ")

index = -1

for i in range(len(s)):
    if s[i] == ch:
        index = i
        break
     
if index == -1:
    print("Character not found.")
else:
    print("Character found at index:", index)
