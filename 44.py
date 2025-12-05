n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # new line
