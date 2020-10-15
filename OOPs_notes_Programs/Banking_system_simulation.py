# Simulating the Banking system

from random import randint


class SavingAccount:
    def __init__(self):
        self.savingaccount = {}

    def create_account(self, name , deposit):
        self.accountnumber = randint(10000,99999)
        self.savingaccount[self.accountnumber] = [name,deposit]
        print("Account created successfully, with and account number", self.accountnumber)

    def authenticate(self,accountnumber, name):
        if accountnumber in self.savingaccount.keys():
            if name == self.savingaccount[accountnumber][0] == name:
                print("Authentication is successful")
                self.display_balance()
                return True
            else:
                print("Provided name is not in our Database,Please check.. Authentication failed")
                return False
        else:
            print("Authentication is failed..!!!")
            return False

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.savingaccount[self.accountnumber][1]:
            print("Insufficient Balance")
        else:
            self.savingaccount[self.accountnumber][1] -= withdraw_amount
            print("Withdrawl is successful")
            self.display_balance()

    def deposit(self,deposit_amount):
        self.savingaccount[self.accountnumber][1] += deposit_amount
        print("Deposit is successful")
        self.display_balance()

    def display_balance(self):
        print("Account Balance amount is:", self.savingaccount[self.accountnumber][1])


savingaccount = SavingAccount()

# Menu Starts Here
while 1:
    print("Enter 1 to create an account")
    print("Enter 2 to access and existing account")
    print("Enter 3 to exit")

    userchoice = int(input())

    if userchoice == 1:
        print("Enter your name:")
        name = input()
        print("Enter Your Deposit amount")
        deposit = float(input())
        savingaccount.create_account(name,deposit)

    elif userchoice == 2:
        print("Enter your 5 digit account number")
        accountnumber = int(input())
        print("Enter your name associated with", accountnumber,"number")
        name = input()
        authentication_status = savingaccount.authenticate(accountnumber,name)
        if authentication_status is True:
            while 1:
                print("Enter 1 to Withdraw the amount")
                print("Enter 2 to Deposit the amount")
                print("Enter 3 to Display the Balance")
                print("Enter 4 for going back to main Menu")
                userchoice = int(input())
                if userchoice == 1:
                    print("Enter the amount to be withdrawn")
                    withdraw_amount = float(input())
                    savingaccount.withdraw(withdraw_amount)
                elif userchoice == 2:
                    print("Enter the amount you want to deposit")
                    deposit_amount = float(input())
                    savingaccount.deposit(deposit_amount)
                elif userchoice == 3:
                    savingaccount.display_balance()
                elif userchoice == 4:
                    break

    elif userchoice == 3:
        quit()

