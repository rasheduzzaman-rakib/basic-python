#xargs
def student(*details):
    print(details[2])

student(7722120080,"Rasheduzzaman",3.66)
student(7722120081,"Asaduzzaman",3.67)
student(7722120082,"Sadiuzzaman",3.68)  


def add(*numbers):
    sum=0 
    for num in numbers:
        sum=sum+num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40,50)    


#xxargs
def student(**details):
   
    print(details["name"])
    print(details["id"])
student(id=101,name="Anis")