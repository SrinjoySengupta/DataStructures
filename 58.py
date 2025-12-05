lst = list(map(int, input("Enter list elements separated by space: ").split()))

unique_list = []
for item in lst:
    if item not in unique_list:
        unique_list.append(item)

print("List after removing duplicates:", unique_list)
