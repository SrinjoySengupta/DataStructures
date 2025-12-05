sum_numbers = 0
count = 0

while True:
    num = float(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break
    
    sum_numbers += num
    count += 1

# Avoid division by zero
if count > 0:
    average = sum_numbers / count
else:
    average = 0

print("Sum of numbers =", sum_numbers)
print("Average =", average)
