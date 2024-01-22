students= (
    "Anisul Islam",
    "Elora",
    "Rashed",
    "Alayna",
    )
    
print(students[0])


tup1 = (50, 'hello', True)
print(tup1[0]) #index checking
print(tup1[1:3]) #slicing

#allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #use len for length

#tuple with one item
thistuple = ("apple",) #must use comma
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))