numbers = {10, 20, 30, 40, 50}
print(type(numbers))
print(numbers)

#empty set vs empty dictionary
empty_set = set()
empty_dict = {}
print(type(empty_set))  # Output: <class 'set'>
print(type(empty_dict))  # Output: <class 'dict'>

#Add and remove elements
skills = {"Python", "Java", "C++"}
skills.add("Machine Learning")
skills.update(["Java", "Data Science"])
print(skills)

skills.remove("C++")  # Raises KeyError if element not found
skills.discard("java") # Does not raise an error if element not found
print(skills)