# Program to calculate Compound Interest

# User inputs
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (in %): "))
time = float(input("Enter Time (in years): "))
n = float(input("Enter number of times interest is compounded per year: "))

# Compound Interest Formula
amount = principal * (1 + rate/(100*n))**(n*time)
compound_interest = amount - principal

# Output
print("Compound Interest:", compound_interest)
print("Total Amount:", amount)
