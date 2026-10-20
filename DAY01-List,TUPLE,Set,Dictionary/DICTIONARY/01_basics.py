student = {
    "name" : "Champion",
    "age" : 20,
    "course" : "Python",
    "Stage" : 1
}
print(student)
print(type(student))

#Accessing values from dictionary
print(student["age"])

#Keys are unique and immutable but values can be mutable and duplicate
data = {
    "a" : 10,
    "b" : 10,
    "c" : 20
}
print(data) #This is valid but keys must be unique, if we try to add duplicate keys it will overwrite the previous value.