from collections import deque

bank=deque(["Anis", "Karim", "Bijoy"]) #hospital e serial joto jon ache

print(bank)

bank.popleft() # 1st pop=anis got service & removed
print(bank) #left 2 person

bank.popleft() # 1st pop=Karim got service & removed
print(bank) #left 1 person

bank.popleft() # 1st pop=Bijoy got service & removed
            #left 0 person

if not bank:
    print("no person left") #no one left after bijoy