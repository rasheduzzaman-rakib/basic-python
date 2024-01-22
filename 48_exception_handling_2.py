try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 / num2
    print(result)
except ValueError:
    print("You have to insert only integer.")
except ZeroDivisionError:
    print("You can not divide a number by 0")
    
finally:
    print("Thanks !!")  
    
    
#
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 / num2
    print(result)
except (ValueError, ZeroDivisionError):
    print("You have entered incorrect input.")
finally:
    print("Thanks !!")
    
    
#
def voter (age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"    

try:
    print(voter(19))
    print(voter(17))
except ValueError as error:
    print(error)