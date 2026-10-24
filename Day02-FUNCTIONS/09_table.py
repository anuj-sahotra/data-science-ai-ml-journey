def print_table(num: int) -> list[str]:
    """Return the multiplication table of a number."""
    
    if isinstance(num, bool) or not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    
    if num < 0:
        raise ValueError("Please enter a positive integer.")
    
    return[f"{num} x {i} = {num * i}" for i in range(1,11)]
    
def user_input() -> int:
    """Taking input from user."""
    while True:
        user_value = input("NUMBER : ").strip()
        
        try:
            number = int(user_value)
        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue

        if number < 0:
            print("Number must be zero or positive.")
            continue

        return number

def main() -> None:
    """Run the table calculator."""
    try:
        number = user_input()

    except (TypeError, ValueError, KeyboardInterrupt) as error:
        print(f"Error : {error}") 
        return
    print("\n".join(print_table(number)))                       
            
if __name__ == "__main__":
    main()                    
            