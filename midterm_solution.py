print("\n=== Student Expense Tracker ===\n")

student_name = input("Enter your name: ")
weekly_budget = float(input("Enter your weekly budget: "))

categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

example_expenses = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi top-up",
    "Notebook, pen, bond paper",
    "Games, movies, hangout"
]

logged_expenses = []
total_spent = 0.0

print("-" * 66)
print(f"| {'#':<3} | {'Category':<20} | {'Example Expenses':<34} |")
print("-" * 66)

for i in range(len(categories)):
    print(f"| {i+1:<3} | {categories[i]:<20} | {example_expenses[i]:<34} |")
print("-" * 66)

for i in range(1, 5):
    print(f"\n--- EXPENSE {i} ---")
    category_number = int(input("Category (1-5 or 0 to skip): "))
    
    if category_number == 0:
        print("Expense slot skipped.")
        continue
    
    if 1 <= category_number <= 5:
        description = input("Description: ")
        amount = float(input("Amount: "))
        
        alert = ""
        if amount > (weekly_budget * 0.25):
            alert = "! High Expense Alert!"
            
        logged_expenses.append([i, categories[category_number-1], description, amount, alert])
        total_spent += amount
    else:
        print("Invalid category. Slot skipped.")

remaining_balance = weekly_budget - total_spent
status = ""
if remaining_balance >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."
