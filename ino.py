class Atm:
    def __init__(self):
        self.__pin=""
        self.__balence=0

        self. __option()
    

    def __option(self):
        user=input("Hello, how would you like to proceed enter 1 to create pin enter 2 to deposite  enter 3 to withdraw enter 4 to check balence enter 5 to exit  ")
        if user=="1":
            self.create_pin()
        elif user=="2":
            self.deposite()
        elif user=="3":
            self.withdraw()
        elif user=="4":
            self.check_balence()
        else:
            print("exit")
    

    def create_pin(self):
        self.__pin=input("enter you pin")
        print("pin set successfully")

    def deposite(self):
        tem=input("enter you pin")
        if tem ==self.__pin:
            amount=int(input("enter the amount"))
            self.__balence=self.__balence+amount
            print("deposite successfully")
        else:
            print("invailed pin")

    def withdraw(self):
        tem=(input("enter your pin"))
        if tem==self.__pin:
            amount=int(input("enter your amount"))
            if amount<self.__balence:
                self.__balence=self.__balence-amount
                print("operation successfully")
            else:
                print("insufficient fund")
        else:
            print("invailed pin")
    def check_balence(self):
        tem=input("enter you pin ")
        if tem==self.__pin:
            print(self.__balence)
        else:
            print("invailed")
    
v=Atm()
# v.deposite()
# v.withdraw()
# v.__balence="1234"
