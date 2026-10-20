a = [10,20,30]
b = a # b is a reference to the same list as a
b[0] = 999
print(a)
print(b)
#b = a; Both variables references to same list object 

#IF WE NEED INDEPENDENT SHALLOW COPY
a = [10, 20, 30]
b = a.copy()
b[0] = 999

print(a) # [10, 20, 30]
print(b) # [999, 20, 30]