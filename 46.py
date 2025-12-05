# Program to calculate the series: 1/1! + 2/2! + ... + n/n!

n = int(input("Enter the value of n: "))

sum_series = 0
fact = 1

for i in range(1, n + 1):
    fact *= i           # compute i! incrementally
    sum_series += i / fact

print("Sum of the series =", sum_series)
