#/usr/bin/python3
class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

# Example usage:
account = BankAccount()
account.deposit(1000)
print("Current balance:", account.get_balance())
