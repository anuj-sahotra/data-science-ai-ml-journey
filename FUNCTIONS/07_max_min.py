def find_maximum(numbers : list[float]) -> float:
    """Return the largest value"""
    
    if not numbers:
        raise ValueError("Numbers can't be empty.")
    return (max(numbers))

def find_minimum(numbers : list[float]) -> float:
    "Return the smallest number."
    
    if not numbers:
        raise ValueError("List can't be empty.")
    
    return (min(numbers))

scores = [100, 50, 65, 150, 65, 185]
print(find_maximum(scores))
print(find_minimum(scores))