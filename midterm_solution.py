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
