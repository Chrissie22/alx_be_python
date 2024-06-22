monthyIncome = int(input("Enter monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthlySavings = monthyIncome - monthly_expenses
annual_interest = 5
projectSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print(f"Your monthy savings are ${monthlySavings}")
print(f"Projected savings after one year, with interest, is: {projectSavings}")