# Print all Armstrong numbers from 100 to 1000

for num in range(100, 1000):
    s = str(num)
    total = 0
    for digit in s:
        total += int(digit) ** 3   # 3 digits → cube

    if total == num:
        print(num)
