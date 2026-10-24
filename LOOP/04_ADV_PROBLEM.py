# WAP to create billing system at supermarket.
def billing_system():
    """Billing system at supermarket."""
    while True:
        name = input("Enter customer name : ")
        while not name:
            name = input("Name cannot be empty. Enter customer name: ").strip()

        total = 0
        while True:
            print("Enter the amount and quantity.")
            
            try:
                amount = float(input("Amount : "))
                quantity = int(input("Quantity : "))
                
            except ValueError:
                print("Invalid input! Please enter valid amount and quantity.")
                continue
            if amount < 0 or quantity <= 0:
                print("Amount must be non-negative and quantity must be at least 1.")
                continue
            total += amount * quantity
                
            more_items = input("Do you want to add more items? (yes/no): ").strip().lower()
            if more_items not in ('yes', 'y'):
                break       
        print("-" * 40)
        print(f"Customer Name: {name}")
        print(f"Total Bill Amount: ${total:.2f}")
        print("-" * 40)
        print("**********Happy Shopping**********")
        
        repeat = input("Do you want to process another customer? (yes/no): ").strip().lower()
        if repeat not in ('yes', 'y'):
            print("Exiting the billing system. Thank you!")
            break   

billing_system()                    
