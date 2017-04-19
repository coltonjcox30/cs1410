
menu=("""What would you like to do?
[r] Record a Book
[f] Find a Book
[l] List all Books
[q] Quit
Enter an option:""")
print (menu)
option=input() 
books = {'978-0439708180':"Harry Potter and the Sorcerer's Stone",'978-0439023528':"The Hunger Games"}
while option!="q":
    if option== "r":
        isbn= input("Enter an ISBN:")
        title= input("Enter a book title:")
        books[isbn]=title
        print ("Book saved!")
        print (menu)
        option=input()
    if option == "f":
        isbn= input("Enter an ISBN:")
        title=books[isbn]
        print ("Book found!:",title)
        print (menu)
        option=input()
    if option == "l":
        i = 1
        for b in books:
            print ("{}) {}: {}".format(i,b, books[b]))
            i+=1
        print (menu)
        option=input()
    
    print ("Bye! Catch ya later!")

