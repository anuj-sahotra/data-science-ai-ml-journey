def reverse_txt(txt):
    """Take an input from user as a string then, reverse it."""
    return txt[::-1]
txt = input("Text : ")
print(f"Reverse of {txt} : {reverse_txt(txt)}")