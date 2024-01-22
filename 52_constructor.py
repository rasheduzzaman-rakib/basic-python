class Student:
    roll=""
    cgpa=""
    
    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    
    def display(self):
        print(f"Roll: {rafi.roll}, CGPA: {rafi.cgpa}")
    
rafi=Student(101,3.75)
rafi.display() 

nafi=Student(102,3.55)
nafi.display()