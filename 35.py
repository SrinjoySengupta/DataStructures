# Print first 20 Fibonacci numbers

a = 0
b = 1

print(a)
print(b)

for _ in range(18):      # already printed first 2 numbers
    c = a + b
    print(c)
    a = b
    b = c
