# Program to find volume of a cylinder and price of milk (1 liter = 40 Rs)

import math

r = float(input("Enter radius of cylinder (in cm): "))
h = float(input("Enter height of cylinder (in cm): "))

# Volume in cubic centimeters
volume_cm3 = math.pi * r * r * h

# Convert cm³ to liters (1000 cm³ = 1 liter)
volume_liters = volume_cm3 / 1000

# Price calculation
price = volume_liters * 40

print("Volume of cylinder in liters:", volume_liters)
print("Price of milk (Rs):", price)
