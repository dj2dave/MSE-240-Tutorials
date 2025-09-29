class BankAccount:
    
    def __init__(self, id): #no need to pass in balance, already has a set value 
        self._id = id
        self._balance = 0
    
    def getId(self):
        return self._id
    def getBalance(self):
        return self._balance 