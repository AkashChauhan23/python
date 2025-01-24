class DepositeChecker:
    def __init__(self):
        self.total_amt = 50

    def amountDisplay(self):
        if self.total_amt > 0:
            print(f'The current balance in your account is {self.total_amt}')
        else:
            raise Exception("No amount left")

    def amountWithdraw(self, withdraw):
        print(f"The withdraw amount is {withdraw}")
        if self.total_amt >= withdraw:
            self.total_amt -= withdraw
            print("Amount withdrawn successfully!")
            self.amountDisplay()
        else:
            raise Exception("Insufficient balance!")

class Depositer(DepositeChecker):
    def __init__(self):
        super().__init__()

    def amountDeposite(self, deposit):
        print(f"The deposit amount is {deposit}")
        self.total_amt += deposit
        print("Amount deposited successfully!")
        self.amountDisplay()

try:
    obj = Depositer()
    obj.amountDisplay()
    obj.amountDeposite(150)
    obj.amountWithdraw(100)
    obj.amountWithdraw(200)
except Exception as e:
    print(e)
