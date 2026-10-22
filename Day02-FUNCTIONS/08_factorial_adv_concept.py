def calculate_factorial(num: int) -> int:
    """Calculate Factorial of a non-negative integer."""
    if isinstance(num, bool) or not isinstance(num, int):
        raise TypeError("Input must be integer.")
    
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, num + 1):
        result = result * i
        
    return result

def get_user_input() -> int:
    """Read and validate an integer from the user."""
    while True:
        user_input = input("Number : ").strip()
        
        try:
            number = int(user_input)
            
            if number < 0:
                print("ERROR! Please enter a non-negative integer.")
                continue
            return number
        except ValueError:
            print("Error! Invalid Input. Enter a whole number.")
            
def main() -> None:
    """Run the factorial calculator."""
    try:
        number = get_user_input()
        answer = calculate_factorial(number)
        
        print(f"Factorial of {number} : {answer}")
        
    except(TypeError, ValueError) as error:
        print(f"Error : {error}")                    
            
if __name__ == "__main__":
    main()        