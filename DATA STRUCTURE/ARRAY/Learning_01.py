import array as arr

val = arr.array('i', [1, 2, 3, 4, 5, 6])
print(val)

print("\n")

#Iteration through loop using range
for i in range(0,6):
    print(val[i], end = " ")

print("\n")

#Iteration through loop using varaible
for x in val:
    print(x, end = " ")    
    