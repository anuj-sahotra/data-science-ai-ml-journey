#Write a program tp find sum of all even numbers upto range n
def sum_even(n):
    """SUM OF EVEN NUMBERS UPTO RANGE n."""
    
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            result += i
            
    return result
even_range = int(input("Range of numbers : "))
print(f"Sum of even numbers upto range {even_range} = {sum_even(even_range)}")            
            
    