# Check if the user makes profit or loss based on CP and SP

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    print("Profit:", sp - cp)
elif sp < cp:
    print("Loss:", cp - sp)
else:
    print("No profit, no loss")
