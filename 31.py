# Program to print all combinations and permutations of [1,2,3,4] manually (no libraries)

nums = [1, 2, 3, 4]

def combinations_manual(arr, index, current):
    if index == len(arr):
        if current:
            print(current)
        return
    combinations_manual(arr, index + 1, current + [arr[index]])
    combinations_manual(arr, index + 1, current)

def permutations_manual(arr, l, r):
    if l == r:
        print(arr)
        return
    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        permutations_manual(arr, l + 1, r)
        arr[l], arr[i] = arr[i], arr[l]

print("Combinations:")
combinations_manual(nums, 0, [])

print("\nPermutations:")
permutations_manual(nums, 0, len(nums) - 1)
