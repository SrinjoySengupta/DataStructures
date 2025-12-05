# Program to calculate n + nn + nnn + ... up to k terms

n = int(input("Enter the value of n: "))
k = int(input("Enter number of terms (k): "))

total = 0
term = ""

for i in range(1, k + 1):
    term = term + str(n)      # build term like n, nn, nnn...
    total += int(term)

print("Sum:", total)
