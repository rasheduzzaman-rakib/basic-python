book=[]
book.append("Learn c")
book.append("Learn c++")
book.append("Learn Java")
print(book)

book.pop()
print("Now the top book is: ",book[-1])

book.pop()
print("Now the top book is: ",book[-1])

book.pop()
if not book:
    print("No book left")