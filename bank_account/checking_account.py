from account import Account

class CheckingAccount(Account):

	def __init__(self,acc_name,acc_num,start_b,od):
		Account.__init__(self,acc_name,acc_num,start_b)
		self.od = od

	def deposit_Money(self,value):
		if value >= 0:
			self.start_b += value
		return
 
	def withdrawl_Money(self,value):
		OD = self.od + self.start_b		
		if value > float(OD):
			print ("INNSUFFICIANT FUNDS!")
		else:
	            self.start_b -= value
	
	
