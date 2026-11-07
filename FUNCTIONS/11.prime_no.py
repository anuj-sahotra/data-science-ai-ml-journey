def is_prime(num):
    """Code to check the whether the number is prime or not."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a Prime Number.")
    
else:
    print(f"{num} is not a Prime Number.")        
        