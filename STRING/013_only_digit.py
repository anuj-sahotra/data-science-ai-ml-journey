#WAP to check if a sting contains only digits.
def is_digits(txt):
    if txt.isdigit():
        return True
    return False

txt = input("Text : ")
if is_digits(txt):
    print("Text contains only digits.")
else:
    print("Not only digits.")     