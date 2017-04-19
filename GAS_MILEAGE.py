menu=("""What would you like to do?
[r] Record Gas consumption
[c] Calculate Gas Mileage
[l] List mileage History
[q] Quit
Enter an option:""")

print (menu)
option=input()
entries=[]

while option != "q":
    if option == "r":
        d = {}
        date = input("What is the date?:")
        d["Date"]= date
        LFU = input("How many miles did you drive since last filling up?:")
        d["Miles"]= LFU
        GA = input("How many gallons of gas did you add to your tank?:")
        d["Gallons"] = GA

        entries.append(d)
        print ("Added!")
               
        print (menu)
        option=input()
    if option == "c":
        if len(entries) <= 0:
            print ("You first need to record your gas consumption!")
        else:
            total= 0
            for e in entries:
                MPG= float(e["Miles"])/float(e["Gallons"])
                total += MPG
            average= total / len(entries)
            print  ("Average gas mileage:",round(average,2))

        print (menu)
        option=input()

    if option == "l":
        for e in entries:
            
            print ("On",e["Date"], e["Miles"], "miles traveled using",e["Gallons"], "gallons.","Average gas mileage:" ,float(e["Miles"])/float(e["Gallons"]))

        print (menu)
        option=input()
        
    if option != "q" or option != "l" or option != "c" or option != "r":
        print ("Sorry, that option is invalid!")

        print (menu)
        option=input()
    
print ("Bye! Catch ya later!")
    
