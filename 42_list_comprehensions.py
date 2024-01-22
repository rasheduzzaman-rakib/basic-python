#normal map function program 
num=[1,2,3,4,5]
result=list(map(lambda x: x*x,num))
print(result)

#same program using list comprehensions 
num=[1,2,3,4,5]
result=[x*x for x in num]
print(result)

#normal filter functon programl
num=[1,2,3,4,5]
result=list(filter(lambda x: x%2==0,num))
print(result)

#same program using list comprehensions
num=[1,2,3,4,5]
result=[x for x in num if x%2==0]
print(result)