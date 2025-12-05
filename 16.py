# Determine weather based on temperature and humidity

temp = float(input("Enter temperature (°C): "))
hum = float(input("Enter humidity (%): "))

if temp >= 30 and hum >= 90:
    print("Hot and Humid")
elif temp >= 30 and hum < 90:
    print("Hot")
elif temp < 30 and hum >= 90:
    print("Cool and Humid")
else:
    print("Cool")
