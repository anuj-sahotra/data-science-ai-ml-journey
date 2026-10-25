def is_palindrome(num):
    """CHECKER WHETHER THE NUMBER IS PALINDROME O0R NOT."""
    if num < 0:
        raise ValueError("Number must be +ve intger.")
    
    original = num
    result = 0
    while num > 0:
        digit = num % 10
        result = (result * 10) + digit
        num //= 10
    return original == result  

num = int(input("Number : "))
if is_palindrome(num):
    print(f"{num} is palindrome.")
else:
    print(f"{num} is not palindrome.")     