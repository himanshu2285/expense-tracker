# print("Basic Expense tracker")

# print("we have to build some good platform")

expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses & Total")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        name = input("Enter expense name (e.g., Food): ")
        try:
            amount = float(input("Enter amount: "))
            expenses.append({"name": name, "amount": amount})
            print(f"Added: {name} - ${amount:.2f}")
        except ValueError:
            print("Invalid amount! Please enter a number.")
            
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            total = 0
            for item in expenses:
                print(f"- {item['name']}: ${item['amount']:.2f}")
                total += item['amount']
            print(f"**Total Spent: ${total:.2f}**")
            
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please pick 1, 2, or 3.")
