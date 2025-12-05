# Program to calculate the series:
# (x-1)/x + 1/2*((x-1)/x)^2 + ... up to n terms

x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

t = (x - 1) / x
sum_series = 0

for k in range(1, n + 1):
    sum_series += (t ** k) / k

print("Sum of the series =", sum_series)
