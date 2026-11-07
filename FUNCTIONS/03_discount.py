def calculate_discount(price, discount_percentage):
    return price * (discount_percentage / 100)
price = float(input("Price : "))
discount_percentage = float(input("Discount % = "))
print(f"Dicount = {calculate_discount(price, discount_percentage)}")