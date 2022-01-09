from nasabah import atm_card

class Customer:
    def __init__(self,id,custPin=1234,custBalance=100000):
        self.id=id
        self.pin=custPin
        self.balance=custBalance
    def CheckId(self):
        return self.id
    def CheckPin(self):
        return self.pin
    def CheckBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self,nominal):
        self.balance += nominal
