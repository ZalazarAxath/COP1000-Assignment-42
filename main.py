# Input
employee_name = input("Employee’s name: ")
num_shifts = int(input("Number of Shifts: "))
num_transactions = int(input("Number of transactions: "))
transaction_value = float(input("Transaction dollar value: "))

# Calculate productivity score
productivity_score = (transaction_value / num_transactions) / num_shifts

# Calculate bonus based on productivity score
if productivity_score <= 30:
    bonus = 50.00
elif 31 <= productivity_score <= 69:
    bonus = 75.00
elif 70 <= productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

# Output
print("Employee Name:", employee_name)
print("Employee Bonus: $" + str(bonus))
