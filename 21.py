# Menu driven program for unit conversions (repeats until 4 is pressed)

while True:
    print("\n--- MENU ---")
    print("1. cm to ft")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cm = float(input("Enter value in cm: "))
        ft = cm / 30.48
        print("Value in feet:", ft)

    elif choice == 2:
        km = float(input("Enter value in km: "))
        miles = km * 0.621371
        print("Value in miles:", miles)

    elif choice == 3:
        usd = float(input("Enter amount in USD: "))
        inr = usd * 83  # approx rate
        print("Value in INR:", inr)

    elif choice == 4:
        print("Exiting program...")
        break   # stops the loop

    else:
        print("Invalid choice! Try again.")
