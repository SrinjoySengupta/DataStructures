# Check if two rectangles overlap

# Rectangle A (x1, y1) = bottom-left, (x2, y2) = top-right
x1 = float(input("Enter A.x1: "))
y1 = float(input("Enter A.y1: "))
x2 = float(input("Enter A.x2: "))
y2 = float(input("Enter A.y2: "))

# Rectangle B
x3 = float(input("Enter B.x1: "))
y3 = float(input("Enter B.y1: "))
x4 = float(input("Enter B.x2: "))
y4 = float(input("Enter B.y2: "))

# If one rectangle is to the left or right of the other → no overlap
if x2 < x3 or x4 < x1:
    print("Rectangles do NOT overlap")
# If one rectangle is above or below the other → no overlap
elif y2 < y3 or y4 < y1:
    print("Rectangles do NOT overlap")
else:
    print("Rectangles OVERLAP")
