import time

class Account:
    def __init__(self, id, custPin = 123456, custBalance = 0):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def checkID(self):
        return self.id

    def checkPin(self):
        return self.pin

    def checkBalance(self):
        return self.balance

    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal

    def countDown(self):
        t = 5
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
