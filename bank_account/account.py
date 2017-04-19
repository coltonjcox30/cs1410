class Account:
	def __init__(self,acc_name,acc_num,start_b):
	        self.acc_name = acc_name
	        self.acc_num = acc_num
	        self.start_b = start_b

	def deposit_Money(self,value):
	        if value >= 0:
	            self.start_b += value
	            return 

	def withdrawl_Money(self,value):
	        self.start_b -= value

	def getBal(self):
		return self.start_b
