# Creating a banking app system

# ------CREATING CLASS-------
# Parent Class: User
class User():
    # Holds details about a user
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Has a function to show user details
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

# Child Class: Bank
class Bank(User):
    # Initialize inheritate from User
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        
        # Stores details about the account balance
        self.balance = 0

    # Stores details about the amount

    # Allows for deposits, withdraw, and view_balance
    def deposit(self, amount):
        self.balance = self.balance + int(amount)
        print("Account balance has been updated: $", self.balance)

    def withdraw(self, amount):
        if int(amount) > self.balance:
            print("Insufficient Funds | Balance Available: $", self.balance)
        else:
            self.balance = self.balance - int(amount)
            print("Account balance has been updated: $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: $", self.balance)

def main():
    print("BANKING SYSTEM APPLICATION")
    johan = Bank('Johan', 21, 'Male')
    print(johan.age)
    print(johan.gender)
    print(johan.name)

    deposit = True
    while deposit:
        deposit_amt = input("The amount you want to deposit: ")
        johan.deposit(deposit_amt)
        done = input("Do you want to do anything else(Y/N)? ")
        if done == 'N':
            deposit = False

    withdraw = True
    while withdraw:
        withdraw_amt = input("The amount you want to withdraw: ")
        johan.withdraw(withdraw_amt)
        done = input("Do you want to do anything else(Y/N)? ")
        if done == 'N':
            withdraw = False

    johan.view_balance()

if __name__ == "__main__":
    main()   