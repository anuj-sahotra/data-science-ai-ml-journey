#Tuple is ordered collection and it is immutable 
student = ("Champion", 23, 100.5)
print(type(student))
print(student)

#Tuple Unpacking
name, age, marks = student
print(name)
print(age)
print(marks)

#Trap of single element tuple 
a = (10)
b = (10,)
print(type(a))
print(type(b))