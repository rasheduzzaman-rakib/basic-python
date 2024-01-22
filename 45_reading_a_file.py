# r=readable, w=write able, r+ = read + Write able, w+ = write + read able
file = open("student.txt","r")
print(file.readable())
file.close()

file=open("student.txt","w")
print(file.writable())
file.close()