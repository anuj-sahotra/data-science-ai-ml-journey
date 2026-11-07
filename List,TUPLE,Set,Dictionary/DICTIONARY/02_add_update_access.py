student = {
    "name" : "Champion",
    "age" : 20,
    "course" : "Python"
}
student["stage"] = 1 #Adding new key-value pair to dictionary
print(student)

#update
student["name"] = "Anuj"
print(student)

#Accessing values from dictionary
print(student.get("course")) #This is a better way to access values from dictionary as it will return None if key is not present instead of throwing an error.