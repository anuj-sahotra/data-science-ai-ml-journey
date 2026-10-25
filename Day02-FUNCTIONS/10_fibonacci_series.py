def fibonacci(n):
    """Write fibonacci series."""
    if n <= 0:
        return []
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Range : "))
print(fibonacci(n))    