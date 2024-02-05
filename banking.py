class BankAcc:
    _funds = 0
    _name = ''
    
    #BankAcc: Constructor
    def __init__(self, name, funds):
        self._funds = funds
        self._name = name
    
    #Method that returns a boolean, it checks if the user has funds or not       
    def haveFunds(self):
        return self._funds > 0
        
    #Method that withdraws the amount given as parameter from user's account    
    def withdraw(self, funds):
        if funds <= self._funds:
            self._funds -= funds
            replaceFundsDetails(str(self._funds))
            print(f"You have a total of {self._funds} in your account")
            operation = f"\nOperation: Withdrawal - Withdrawn {funds}$ from {self._name}'s Account"
            appendToDetails(operation)
        else:
            print(f"You don't have enough funds. Total funds: {self._funds}")
    
    #Method that deposits the amount given as parameter to user's account    
    def deposit(self, funds):
        self._funds += funds
        replaceFundsDetails(str(self._funds))
        operation = f"\nOperation: Deposit - Deposited {funds}$ to {self._name}'s Account"
        appendToDetails(operation)
        print(f"You have a total of {self._funds} in your account")


#========================================================================================

#Function that recieves a string to append to the bank account details
def appendToDetails(toAppend):
    with open("bankAccDetails.txt", 'a') as file:
        file.write(toAppend)    

#Function that changes the total funds at the bank account details            
def replaceFundsDetails(toReplace):
    with open("bankAccDetails.txt", 'r') as file:
        lines = file.readlines()
    
    lines[1] = toReplace + '\n'
    
    with open("bankAccDetails.txt", 'w') as file:
            file.writelines(lines)

#========================================================================================

accData = ''

with open('bankAccDetails.txt', 'r') as bankFile:
    accData = bankFile.readlines()


myAcc = BankAcc('User', int(accData[1]))

while True:
    operation = input(f"Welcome to DJ & V Bank {myAcc._name}, select operation [W: Withdrawal/D: Deposit/E: Exit]: ").upper()
    
    if operation == 'W':
        if myAcc.haveFunds():
            try:
                toWithdraw = int(input("How much money do you want to withdraw?: "))
            except Exception:
                print("The Value provided is not a number")
            myAcc.withdraw(toWithdraw)
        else:
            print("You don't have any funds")

        
    elif operation == 'D':
        try:
            toDeposit = int(input("How much money do you want to deposit?: "))
        except Exception:
            print("The value submitted is not a number")
        myAcc.deposit(toDeposit)
    elif operation == 'E':
        quit()
    else:
        print('Invalid operation')
        continue