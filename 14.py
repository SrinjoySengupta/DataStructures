# Program to find the angle between hour and minute hand

h = int(input("Enter hour (1–12): "))
m = int(input("Enter minutes (0–59): "))

# Convert hour to 12-hour format
h = h % 12

# Formula:
# Hour hand moves 0.5 degrees per minute
# Minute hand moves 6 degrees per minute
hour_angle = 30*h + 0.5*m
minute_angle = 6*m

# Find absolute difference
angle = abs(hour_angle - minute_angle)

# Smaller angle between the two hands
angle = min(angle, 360 - angle)

print("Angle between hour and minute hand:", angle)
