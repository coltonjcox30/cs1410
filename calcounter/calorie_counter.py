from The_calorie_counter import Calorie_Counter
def main():
	print ("""Hi! This program will calculate your caloric balance for the day!
Before we can start, I need some information about you. Be honest! :)""")

Gender = input("What is your gender (F or M)?")
Age = input("What is your age?")
Height = input("What is your height in inches?")
Weight = input("What is your weight in pounds?")
option = ""

counter = Calorie_Counter(Height,Weight,Age,Gender)

print ("Thanks! Now, throughout the day, tell me each time you eat or move. Your caloric balance is starting at" ,'{:0.0f}'.format(counter.CurrentBalance()), "(you need to eat something!)")

Rmenu= ("""What would you like to do?
[f] Record Food Consumption
[a] Record Physical Activity
[q] Quit""")

Amenu= ("""Choose an activity to record:
[1] Climbing hills (22lb. load)
[2] Cooking
[3] Run
[4] Squats
[5] Free Weights""")

print (Rmenu)
option = input("Enter an option: ")

while option != "q":
    if option == "f":
        C=input ("Okay! How many calories did you just eat?")
        counter.AddCal(C)
        print ("Your caloric balance is now" ,'{:0.0f}'.format(counter.CurrentBalance()))
        
        print (Rmenu)
        option = input("Enter an option: ")
    if option == "a":
        print (Amenu)
        A= input ("Choose an activity to record:")
        if A == '1':
            M = int(input("For how many minutes did you perform this activity?"))
            counter.Exercise(.064 , M)
            print ("Awesome! Your caloric balance is now:" ,'{:0.0f}'.format(counter.CurrentBalance()))

            print (Rmenu)
            option = input("Enter an option: ")

        elif A == '2':
            M = int(input("For how many minutes did you perform this activity?"))
            counter.Exercise(.022 , M)
            print ("Awesome! Your caloric balance is now:" ,'{:0.0f}'.format(counter.CurrentBalance()))

            print (Rmenu)
            option = input("Enter an option: ")

        elif A == '3':
            M = int(input("For how many minutes did you perform this activity?"))
            counter.Exercise(.095 , M)
            print ("Awesome! Your caloric balance is now:" ,'{:0.0f}'.format(counter.CurrentBalance()))

            print (Rmenu)
            option = input("Enter an option: ")

        elif A == '4':
            M = int(input("For how many minutes did you perform this activity?"))
            counter.Exercise(.096 , M)
            print ("Awesome! Your caloric balance is now:" ,'{:0.0f}'.format(counter.CurrentBalance()))

            print (Rmenu)
            option = input("Enter an option: ")

        elif A == '5':
            M = int(input("For how many minutes did you perform this activity?"))
            counter.Exercise(.039 , M)
            print ("Awesome! Your caloric balance is now:" ,'{:0.0f}'.format(counter.CurrentBalance()))

            print (Rmenu)
            option = input("Enter an option: ")
	







