num={1,2,3,4,5,5,6,6,77}
print(num)


#set conversion
num1={1,2,3,4,5,5,6,6,77}
num2=set([1,2,3,4,5,5,6,6,77])
print(num2)


#number add & remove
num1={1,2,3,4,5,5,6,6,77}
num2=set([1,2,3,4,5,5,6,6,77])
num2.add(7)
num2.remove(7)
print(num2)
print(4 in num2)


#
num1={1,2,3,4,5}
num2=set([4,5,6])

print(num1 | num2) #union
print(num1 & num2) #intersection
print(num1 - num2) #difference 