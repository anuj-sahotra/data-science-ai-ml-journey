numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]  # List comprehension to create a list of squares
print(squares)  # Output: [1, 4, 9, 16, 25]

even_numbers = [n for n in numbers if n % 2 == 0]  # List comprehension to filter even numbers
print(even_numbers) # Output: [2, 4]