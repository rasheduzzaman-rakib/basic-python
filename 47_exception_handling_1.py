#error
num2= input("Enter a number: ")
result= 20/num2
print(result)
print("Done")

#int added
num2= int(input("Enter a number: "))
result= 20/num2
print(result)
print("Done")


#ZeroDivisionError
try:
    list=[20,0,30]
    result=list[0]/list[1]
    print(result)
    print("Done")
#the following line will handle the error
except ZeroDivisionError:
    print("Dividing by zero is not possible")
print("Successfull")

#IndexError
try:
    list=[20,0,30]
    result=list[0]/list[1]
    print(result)
    print("Done")
#the following line will handle the error
except IndexError:
    print("Index Error")
print("Successfull")

