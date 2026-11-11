from datetime import datetime

expenses = [] #Expenses store in the list 
CATEGORIES = ["FOOD", "TRAVEL", "ENTERTAINMENT", "SHOPPING", "OTHERS"]

def get_date():
    """Returns the date of the expenditure."""
    while True:
        date = input("Date (DD-MM-YYYY) : ").strip()
        try:
            datetime.strptime(date, "%d-%m-%Y") # Matching the date format with the given format
            return date
        except ValueError:
            print("Invalid date format. Please enter in DD-MM-YYYY format.\n")

def get_category():
    """Returns the category of the expenditure."""
    
    while True:
        print("Select a category from the following:")
        for idx, category in enumerate(CATEGORIES, start=1):
            print(f"{idx}. {category}")
        
        user_input = input("Enter the category number : ").strip()
        if user_input.isdigit() and 1 <= int(user_input) <= len(CATEGORIES): # Checking if the user input is a valid category number
            return CATEGORIES[int(user_input) - 1]
        else:
            print("Invalid category number. Please try again.\n")
            
def get_amount():
    """Returns the amount of the expenditure."""
    
    while True:
        try:
            amount = float(input("Enter the amount : ").strip())
            if amount < 0:
                print("Amount cannot be negative. Please enter a valid amount.")            
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            
def add_expenses():
    """Returns the details of the expenditure."""
    
    date = get_date()
    category = get_category()
    description = input("Give more detail : ").strip()
    amount = get_amount()
    
    expense = {
        "date" : date,
        "category" : category,
        "description" : description,
        "amount" : amount
    }
    expenses.append(expense)
    
    print("\nExpenses added successfully !!")
    
def view_expenses():
    """Returns the details of all expenses."""
    
    if len(expenses) == 0:
        print("\nNo expenses found !!")
        return
    
    for count, each_expenditure in enumerate(expenses, start = 1):
        print(f"\n{'='*5} EXPENSE {count} {'=' * 5}")
        print(f"Date : {each_expenditure['date']}")
        print(f"Category : {each_expenditure['category']}")
        print(f"Description : {each_expenditure['description']}")
        print(f"Amount : {each_expenditure['amount']:.2f}")
    
def total_spending():
    """Returns the total amount spent."""
    total = sum(each_expenditure["amount"] for each_expenditure in expenses)
    
    print(f"\nTotal amount : {total:.2f}")

def menu():
    """Main menu for the expense tracker."""
    print("EXPENSE TRACKER")
    
    while True:
        print(f"\n{'='*5} MENU {'=' * 5}")
        print("""
            1. Add Expense
            2. View All Expenses
            3. View Total Spending
            4. Exit
            """)
        
        user_input = input("Enter your choice (1-4) : ").strip()
            
        if user_input == "1":
            add_expenses()
        elif user_input == "2":
            view_expenses()
        elif user_input =="3":
            total_spending()
        elif user_input == "4":
            print("Thank you !!")
            break
        else:
            print("Invalid Input")

# The program starts executing from here        
if __name__ == "__main__":
    menu()                