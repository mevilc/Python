# Bank Account
import random

class User:
    def __init__(self):
        ''' initialization function '''
        # Attributes supplied by user, therefore no parameters needed
        # validates the user input, only then assigns them to be an attribute
        name = input("Enter name: ")
        self.setName(name)
        DOB = input("Enter date (mm/dd/yyyy): ")
        self.setDOB(DOB)
        balance = float(input("Enter balance: "))
        print()
        self.setbalance(balance)
        self.account_num=random.randint(100000, 999999)
        # prints a statement about account creation
        print("An account with name '" + self.name + "' and an account number " + str(self.account_num) +
              " is created with a balance of $" + str(self.balance) + "\n")

    # Getter Functions
    def getName(self):
        ''' Returns name of account holder'''
        return self.name

    def getDOB(self):
        ''' Returns DOB of account holder '''
        return self.DOB

    def getBalance(self):
        ''' Returns balance of account holder '''
        return self.balance

    def getAccountNum(self):
        ''' Returns the account number of account holder '''
        return self.account_num

    # Setter Functions
    # While loop loops through until the user input is validated. Once validated, while loop stops.
    def setName(self, name):
        ''' Validates a new account name '''
        nameflag=True
        while nameflag:
            if name.isdigit() != True: # checks if name input is all strings
                self.name = name
                nameflag=False
            else:
                print("Please enter a valid name")
                name = input("Enter name: ")

    def setDOB(self, DOB):
        ''' Validates a new account DOB '''
        DOBflag = True
        while DOBflag:
            if (len(DOB) == 10) and (DOB[:2] >= "01" and DOB[:2] <= "12") and (DOB[3:5] >= "01" and DOB[3:5] <= "31") \
                    and (int(DOB[6:10]) >= 1900 and int(DOB[6:10]) <= 9999):
                self.DOB = DOB
                DOBflag=False
            else:
                print("Please enter a valid date")
                DOB = input("Enter date (mm/dd/yyyy): ")


    def setbalance(self, balance):
        ''' Validates a new account balance '''
        balanceflag=True
        while balanceflag:
            if type(balance) != str: # checks if balance amount is not a string
                self.balance = balance
                balanceflag = False
            else:
                print("Please enter a valid balance amount")
                balance = float(input("Enter balance: "))

    def deposit(self, dep_value):
        ''' Deposits money into account '''
        self.balance += dep_value  # adds value to balance
        print("\nYou have added $" + str(dep_value) + " to your account. Your Balance is $" + str(round(self.balance,2)) + ".")

    def withdraw(self,with_value):
        ''' Withdraws money from account '''
        # checks if account balance is sufficient for withdrawal
        if self.balance >= with_value:
            self.balance-=with_value  # subtracts value from balance
            print("You have $" + str(self.balance) + "remaining in your account." )
        else: # if not sufficient
            not_enough=input("You dont have enough balance to withdraw that amount. Would you like to withdraw less money (Y/N)?\n")
            if not_enough == "Y":
                with_less = float(input("How much money do you want to withdraw? "))
                self.balance-=with_less
                print("You have $" + str(round(self.balance,2)) + " remaining in your account.")
            elif not_enough == "N":
                pass

# Loops through the list of users to check if a user exist
def access_account(list_of_user):
    ''' Finds if there is an account with a name given by user '''
    # loops through to check if name given is in system
    count = 0  # keeps track of when the account name is not in the system
    for user in list_of_user:
        if user.getName() == user_name:  # if name found in list, print all the info about the user.
            print("Hello " + user.getName() + ". Your DOB is " + user.getDOB() + " and your account number is " + str(
                user.getAccountNum()) +
                  " . You have $" + str(user.getBalance()) + " in your account\n")
            # then ask what they want to do - deposit or withdraw
            access = int(input("Do you want to deposit (1) or withdraw (2) money? "))
            if access == 1:
                dep = float(input("How much do you want to deposit? "))
                user.deposit(dep)
            elif access == 2:
                remove = float(input("How much do you want to withdraw? "))
                user.withdraw(remove)
        # if account with name not found, track how many times
        else:
            count += 1

    if count == len(list_of_user):
        print("An account with that name does not exist.\n")


################ MAIN CODE #######################

list_of_user = []  # keeps track of all users
user_input = 0  # just to get into while loop

print("\nWELCOME TO THE BANK\n")
while user_input != "4":
    user_input = input("(1) Create an account,\n(2) access an existing account,\n(3) see all users, or \n(4) exit\n")

    # if user wants to make a new account, make a new instance (object) of the class and add it to the list
    if user_input == "1":
        user1 = User()
        list_of_user.append(user1)

    # if user wants to access existing account, check list and ask what next to do
    elif user_input == "2":
        user_name = input("Enter the name of the account: ")
        # loops through to check if name given is in system
        access_account(list_of_user)

    # if user wants to see all users in bank, access every instance in list and get info for each one
    elif user_input == "3":
        if len(list_of_user) == 0:
            print("There are no accounts yet.\n")
        else:
            print("These are all the accounts in this Bank: \n")
        for user in list_of_user:
            print("Name: " + user.getName() + ", DOB: " + user.getDOB() + ", Balance: $" + str(user.getBalance()) +
                  ", Account Number: " + str(user.getAccountNum()))

    # if user does not enter one of the options
    elif user_input not in "1234":
        user_input = input("Please enter a valid option."
                           " \n(1) Create an account,\n(2) access an existing account,\n(3) see all users, or \n(4) exit\n")


print("\nThank you for using the Bank")