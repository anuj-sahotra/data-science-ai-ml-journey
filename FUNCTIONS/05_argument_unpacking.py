def multiply(a, b, c):
    return a * b * c
numbers = [5, 5, 5]
print(multiply(*numbers))

#UNPACKING **KWARGS
def introduce(name, age):
    return f"{name} is {age} years old."
person = {"name" : "Champion", "age" : 23}
print(introduce(**person))