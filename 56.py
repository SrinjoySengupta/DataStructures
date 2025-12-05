s = input("Enter a string: ")
ch = input("Enter character to remove: ")

result = ""

for c in s:
    if c != ch:
        result += c

print("String after removal:", result)
