#Write a program to find sum of  odd number upto range n

def sum_odd(n):
    """Sum of ODD Numbers upto range n."""
    
    result = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            result += i
    return result
odd_range = int(input("Range of numbers = "))
print(f"Sum of Odd numbers upto range {odd_range} = {sum_odd(odd_range)}")        