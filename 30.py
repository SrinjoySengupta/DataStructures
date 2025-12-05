# Program to calculate population after given years with 10% annual growth

population = 1000
years = int(input("Enter number of years: "))

for _ in range(years):
    population += population * 0.10   # increase by 10%

print("Population after", years, "years =", int(population))
