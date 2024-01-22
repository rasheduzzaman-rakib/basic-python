# 1 len function
subjects=["c","c++","java"]
print(len(subjects)) #length  ber korar jonno use kore len


# 2 append function
subjects=["c","c++","java"]
subjects.append ("TOC") #append will add a value after the full list.
print (subjects)


# 3 insert functon
subjects=["c","c++","java"]
subjects.insert(2,"OS") # insert will add a value the point you want
print(subjects)


# 4 remove function
subjects=["c","c++","java"]
subjects.remove("c") # remove will remove your indicated listed value
print(subjects)

# 5 sort function(sajano)
subjects=["BASIC","R","c","c++","java"]
subjects.sort()
print(subjects)


subjects=[2,87,64,1,4,567,9077,3456744]
subjects.sort()
print(subjects)


# 6 reverse function
subjects=[2,87,64,1,4,567,9077,3456744]
subjects.reverse()
print(subjects)


# 7 pop function
subjects=[2,87,64,1,4,567,9077,3456744]
subjects.pop()
print(subjects)


# 8 clear function
subjects=[2,87,64,1,4,567,9077,3456744]
subjects.clear()
print(subjects)


# 9 copy function
subjects = [2,87,64,1,4,567,9077,3456744]
subjects2 = subjects.copy()
print(subjects2)


# 10 index function
subjects = [20,10,4,555]
pos=subjects.index(4)
print(pos)


# 11 count function
subjects = [20,10,4,555,4,9,0,4,4,89,54,4]
pos=subjects.count(4)
print(pos)