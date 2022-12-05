"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract="", hours="", commission="", hourlyPay="", salaryPay="", fixedCommission="", noContracts="", contractPay=""):
        self.name = name
        self.contract = contract
        self.hours = hours
        self.commission = commission
        self.hourlyPay = hourlyPay
        self.salaryPay = salaryPay
        self.fixedCommission = fixedCommission
        self.noContracts = noContracts
        self.contractPay = contractPay

    def contract_pay(self):
        if self.contract == 'monthly':
            return self.salaryPay
        else:
            return self.hourlyPay * self.hours

    def commission_pay(self):
        if self.commission == 'bonus':
            return self.fixedCommission
        else:
            return self.noContracts * self.contractPay

    def get_pay(self):
        totalPay = self.contract_pay()
        if self.commission:
            totalPay += self.commission_pay()
        return totalPay

    def __str__(self):
        printStr = f"{self.name} works on a "
        if self.contract == 'monthly':
            printStr += f"monthly salary of {self.contractPay}"
        else:
            printStr += f"contract of {self.hours} hours at {self.hourlyPay}/hour"
        if self.commission:
            if self.commission == 'bonus':
                printStr += f" and receives a bonus commission of {self.fixedCommission}."
            else:
                printStr += f" and receives a commission for {noContracts} contract(s) at {contractPay}/contract."
        printStr += f" Their total pay is {self.get_pay()}."
        print(printStr)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', salaryPay=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourlyPay=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', salaryPay=3000, commission="commission", noContracts=4, contractPay=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourlyPay=25, commission="commission", noContracts=3, contractPay=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', salaryPay=2000, commission='bonus', fixedCommission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourlyPay=30, commission='bonus', fixedCommission=600)
