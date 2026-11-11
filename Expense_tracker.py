
# Personal Expense Tracker

print("PERSONAL EXPENSE TRACKER")

# Taking first expense
expense1 = input("Enter first expense name: ")
amount1 = float(input("Enter amount: "))

# Taking second expense
expense2 = input("Enter second expense name: ")
amount2 = float(input("Enter amount: "))

# Taking third expense
expense3 = input("Enter third expense name: ")
amount3 = float(input("Enter amount: "))



print("\nYOUR EXPENSES")

print(expense1, "-", amount1)
print(expense2, "-", amount2)
print(expense3, "-", amount3)


total = amount1 + amount2 + amount3

print("\nTOTAL EXPENSES:", total)

