# Sum of 3 digits of different data types

a = int(input("Enter first digit (int): "))          # integer
b = float(input("Enter second digit (float): "))     # float
c = input("Enter third digit (string digit): ")      # string

sum_digits = a + b + int(c)   # convert string digit to int

print("Sum of the three digits:", sum_digits)
