numbers = [1, 2, 3, 4, 5]
squares = {n : n ** 2 for n in numbers}
print(squares)

even_squares = {n : n ** 2 for n in numbers if n % 2 == 0}
print(even_squares)