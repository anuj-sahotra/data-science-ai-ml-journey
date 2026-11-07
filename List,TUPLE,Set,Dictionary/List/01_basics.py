#Creating List and accessing elements
my_list = [1, 2, 3, 4, 5]
print(my_list)

#Type printing
print(type(my_list))

#Accessing elements
print(my_list[0])  # Accessing first element
print(my_list[2])  # Accessing third element
print(my_list[-1]) # Accessing last element 


#MUTABLE: Lists are mutable, meaning you can change their content without changing their identity.
my_list[1] = 100 
print(my_list)  # Output: [1, 100, 3, 4, 5]

#Clear the list
print(my_list.clear())  # Output: []