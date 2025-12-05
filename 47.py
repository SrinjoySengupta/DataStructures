# Program to calculate the series: 1 + x^2/2 + x^3/3 + ... + x^n/n

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

sum_series = 1  # first term is always 1

for i in range(2, n + 1):
    sum_series += (x ** i) / i

print("Sum of the series =", sum_series)
