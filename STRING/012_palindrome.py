def is_palindrome(txt):
    """Code to check whether the string is Palindrone or not."""
    return txt == txt[::-1]

txt = input("Text : ").lower()
if is_palindrome(txt):
    print("Palindrome.")
    
else:
    print("Not Palindrome.")    