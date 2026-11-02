from array import *

# 'd' -> for storing float value
val = array('d', [1, 2, 3, 4, 5, 6, 9.7, 7.3])

for i in range(0, len(val)):
    print(val[i])
    
#For typecode -> d -> float    
print(val.typecode) 

#reverse
val.reverse()
for i in range(0, len(val)):
    print(val[i], end = " ")
    