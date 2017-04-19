from checking_account import CheckingAccount
from savings_account import SavingsAccount

def initial():
	Acc_menu = input("""What type of account would youl like to track?
	[c] Checkings
	[s] Savings
	Enter an option: """)
	if Acc_menu == "c":
		checking_A()		
	if Acc_menu == "s":
		savings_A()	

def checking_A():
	check = 1
	#x = round(start_b,2)
	print ("Great! I need some information to start:")
	acc_name = input("What is the name of the account holder? ")
	acc_num = input("What is the account number? ")
	start_b = input("What is the starting balance? $")
	od = input("What is the overdraft limit? $")
	user = CheckingAccount(acc_name,float(acc_num),float(start_b),float(od))
	while check == 1:
		checking_Option_menu = input("""What would you like to do?
			[d] Deposit
			[w] Withdraw
			[q] Quit
			Enter an option: """)
		if checking_Option_menu == "d":
			value = input("How much would you like to deposit? $")		
			user.deposit_Money(float(value))
			print ("Your account balanace is now $" + str(round(user.getBal(),2)) + ".")
			
		if checking_Option_menu == "w":
			value = input("How much do you want to withdraw? $")
			user.withdrawl_Money(float(value))
			print ("Your account balanace is now $" + str(round(user.getBal(),2)) + ".")			
		
		if checking_Option_menu == "q":
			print ("Your final account balance is $" + str(round(user.getBal(),2)) + ",have a great day!")
			check = 0
			break
option = ""

def savings_A():
	check = 1
	print ("Great! I need some information to start:")
	acc_name = input("What is the name of the account holder? ")
	acc_num = input("What is the account number? ")
	start_b = input("What is the starting balance? $")
	ir = input("What is the interest rate? " + "%")
	user = SavingsAccount(acc_name,float(acc_num),float(start_b),float(ir))
	while check == 1:	
		savings_Option_menu = input("""What would you like to do?
		[d] Deposit
		[w] Withdraw
		[a] Add monthly interest
		[q] Quit
		Enter an option:""")
	
		if savings_Option_menu == "d":
			value = input("How much would you like to deposit? $")
			user.deposit_Money(float(value))
			print ("Your account balanace is now $" + str(round(user.getBal(),2)) + ".")
		
		if savings_Option_menu == "w":
			value = input("How much do you want to withdraw? $")
			user.withdrawl_Money(float(value))
			print ("Your account balanace is now $" + str(round(user.getBal(),2)) + ".")

		if savings_Option_menu == "a":
			user.monthlyIR()
			print ("Your account balanace is now $" + str(round(user.getBal(),2)) + ".")	
		

		if savings_Option_menu == "q":
			print ("Your final account balance is $" + str(round(user.getBal(),2)) + ",have a great day!")
			check = 0
			break
	option = ""


initial()


