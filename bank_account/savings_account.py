from account import Account

class SavingsAccount(Account):

	def __init__(self,acc_name,acc_num,start_b,ir):
	        Account.__init__(self,acc_name,acc_num,start_b)
	        self.ir = ir

	def deposit_Money(self,value):
        	if value >= 0:
        	    self.start_b += value
        	    return 

	def withdrawl_Money(self,value):
	        if self.start_b - value < 0:
	            print ("INNSUFFICIANT FUNDS!")
	        else:
	            self.start_b -= value
	
		
	
	def monthlyIR(self):
		I = float(self.ir / 100 / 12) * self.start_b
		self.start_b += I
		return
