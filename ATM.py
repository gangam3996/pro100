class Atm(object):
	def __init__(self,cardno,pin):
		self.cardno = cardno
		self.pin = pin

	
	def cashwidrawl(self):
		print("Casg Withdrawn")

	def BalanceEnquiry(self):
		print("Balnce enquiry")

user1 = Atm(123,234)

print(user1.BalanceEnquiry())
																																	