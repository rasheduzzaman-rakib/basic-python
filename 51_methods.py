class Student:
    roll=""
    cgpa=""
    
    
    def display(self):
        print(f"Roll: {rafi.roll}, CGPA: {rafi.cgpa}")
    
rafi=Student()
rafi.roll=101
rafi.cgpa=3.5
rafi.display()


nafi=Student()
nafi.roll=102
nafi.cgpa=3.6
nafi.display()


#methods
class Student:
    roll=""
    cgpa=""
    
    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    
    def display(self):
        print(f"Roll: {rafi.roll}, CGPA: {rafi.cgpa}")
    
rafi=Student()
rafi.set_value(101,3.75)
rafi.display() 

nafi=Student()
nafi.set_value(102,3.55)
nafi.display()