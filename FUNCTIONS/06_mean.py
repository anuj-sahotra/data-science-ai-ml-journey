def calculate_mean(*numbers):
    """Return the arithmetic mean of a non - empty list."""
    if not numbers:
        raise ValueError("Numbers cannot be empty.")
    return sum(numbers) / len(numbers)

scores = [80, 90, 70]
print(calculate_mean(*scores))