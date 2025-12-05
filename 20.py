# Program to calculate in-hand salary after deductions:
# HRA = 10%, DA = 5%, PF = 3%
# Tax slabs:
# 0–1 lakh  → print "k" (no tax)
# 5–10 lakh → 10%
# 11–20 lakh → 20%
# >20 lakh → 30%

salary = float(input("Enter your annual salary: "))

# Basic deductions
hra = 0.10 * salary
da  = 0.05 * salary
pf  = 0.03 * salary

# Calculate tax based on slabs
if salary <= 100000:
    print("k")         # as per your instruction
    tax = 0
elif 500000 <= salary <= 1000000:
    tax = 0.10 * salary
elif 1100000 <= salary <= 2000000:
    tax = 0.20 * salary
elif salary > 2000000:
    tax = 0.30 * salary
else:
    tax = 0  # salary between 1–5 lakh has no tax as per your rules

# Total deductions
total_deduction = hra + da + pf + tax

# In-hand salary
in_hand = salary - total_deduction

print("HRA Deduction:", hra)
print("DA Deduction:", da)
print("PF Deduction:", pf)
print("Tax Deduction:", tax)
print("In-hand Salary:", in_hand)
