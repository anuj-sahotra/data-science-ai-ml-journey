def show_menu():
    print(f"{'*' * 10} CALCULATOR {'*' * 10}")
    print("""
    OPERATIONS YOU CAN PERFORM:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Integer Division (//) -> Gets the quotient of the division
    6. Power (**) -> Raises the first number to the power of the second
    7. Modulus (%) -> Gets the remainder of the division
    """)
    
#These block of functions perform the basic arithmetic operations and return the result in a formatted string    
def add(num1,num2):
    return f"{num1} + {num2} = {num1 + num2}"

def subtract(num1,num2):
    return f"{num1} - {num2} = {num1 - num2}"

def multiply(num1,num2):
    return f"{num1} * {num2} = {num1 * num2}"

def divide(num1,num2):
    if num2 == 0:
        return "Error! Division by zero."
    return f"{num1} / {num2} = {num1 / num2}"

def get_quotient(num1,num2):
    if num2 == 0:
        return "Error! Division by zero."
    return f"{num1} // {num2} = {num1 // num2}"

def power(num1,num2):
    if num2 < 0:
        return "Error! Negative exponent."
    try:
        return f"{num1} ** {num2} = {num1 ** num2}"
    except OverflowError:
        return "Error! Result is too large."

def get_remainder(num1,num2):
    if num2 == 0:
        return "Error! Division by zero."
    return f"{num1} % {num2} = {num1 % num2}"

OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '//': get_quotient,
    '**': power,
    '%': get_remainder
}
def calculate(num1, operator, num2):
    if operator not in OPERATIONS:
        return "Invalid operator. Please use one of the following: +, -, *, /, //, **, %"
    return OPERATIONS[operator](num1, num2)

#This function gets the user input for the two numbers and the operator
def get_user_input():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, //, **, %): ").strip()
        num2 = float(input("Enter second number: "))
        return num1, operator, num2
    except ValueError: # Catches the ValueError exception if the user enters a non-numeric value
        return None
    
def main():
    show_menu()
    while True:
        values = get_user_input()
        if values is None:
            print("Invalid input. Please enter numeric values.")
            continue
        num1, operator, num2 = values
        result = calculate(num1, operator, num2)
        print(result)
        
        retry = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if retry not in ('yes', 'y'):
            print("Thank you for using the calculator. Goodbye!")
            break
 
if __name__ == "__main__":
    main()    