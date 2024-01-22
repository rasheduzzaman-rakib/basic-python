def calculate(a,b): #named function
    return a*a + 2*a*b + b*b

print(calculate(2,3))

#lamda function ( anonymous function ) ? single line code
print((lambda a,b : a*a + 2*a*b + b*b ) (2,3))


a=(lambda a,b : a*a + 2*a*b + b*b ) (2,3)
print(a)

#cube
print((lambda x: x*x*x)(2))

a=(lambda x: x*x*x)(3)
print(a)