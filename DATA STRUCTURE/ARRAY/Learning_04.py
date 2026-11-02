from array import *

val = array('i', [1, 2, 3, 4, 5, 6])

#Copy an array
copyArray = array(val.typecode, (x for x in val))

for i in range(0,len(copyArray)):
    print(copyArray[i], end=" ")
    
print("\n")    
#Delete element in array using pop(index) and if index is not give last element automatically deleted
copyArray.pop(1)
for y in copyArray:
    print(y, end= " ")
    
print("\n")    
    
#remove(element)
copyArray.remove(1)
for y in copyArray:
    print(y, end= " ")    