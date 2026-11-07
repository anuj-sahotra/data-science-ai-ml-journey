fruits = ["Orange", "Apple", "Litchi", "Banana"]
print(len(fruits))

for i in fruits:
    print(i)
    
#Iteration using for loop with range and length function    
for i in range(len(fruits)):
    print(fruits[i])    
    
print("-" * 30)    
#Iteration using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
    
print("-" * 30)
# Short - Hand for loop
[print (i) for i in fruits]    

print("-" * 30)
# Reverse the list
fruits.reverse()
print(fruits)

print("-" * 30)
#Sort 
fruits.sort()
print(fruits)

print("-" * 30)
#Append 
fruits.append("Guava")
print(fruits)
        