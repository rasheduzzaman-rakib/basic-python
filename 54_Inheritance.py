class Phone: #super class, parent class, Base class
    def call(self):
        print("You can call")
        
    def message(self):
        print("You can message")
        
class Samsung(Phone):#sub classs, child class, derived class
    def photo(self):
        print("You can take photo")    
    
p=Phone()
p.message() 
p.call()

s=Samsung()
s.message() 
s.call()
s.photo()

print(issubclass(Samsung,Phone))#samsung class ta holo phone class er ekta sub class
print(issubclass(Phone, Samsung))