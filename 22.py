# Given total heads and total legs, find number of dogs and chickens
# Chickens have 2 legs, Dogs have 4 legs

heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

# Let:
# c = number of chickens
# d = number of dogs
# c + d = heads
# 2c + 4d = legs

# Solve equations:
# From c = heads - d
# Substitute -> 2(heads - d) + 4d = legs

d = (legs - 2*heads) // 2   # number of dogs
c = heads - d               # number of chickens

if d < 0 or c < 0 or (2*c + 4*d) != legs:
    print("No valid solution")
else:
    print("Number of chickens:", c)
    print("Number of dogs:", d)
