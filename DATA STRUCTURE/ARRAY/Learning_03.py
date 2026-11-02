from array import *

val = array('i', [1,2,3,4,5,6,7,8])

#Reverse an array
val.reverse()
for i in val:
    print(i, end = " ")
    
print("\n")

#Insesrt element using index array_name.insert(index, value to be add)    
val.insert(1, 50)
for i in val:
    print(i, end = " ")
        
print("\n")

#Add element at the end using append         
val.append(100)
for x in val:
    print(x, end=" ")
