# WAP to write first n numbers with their square

def num_square(num):
    """Print number with their Square."""
    for i in range(1,num + 1):
        print(f"{i} : {i ** 2}")
    
num_range = int(input("Range : "))
num_square(num_range) 