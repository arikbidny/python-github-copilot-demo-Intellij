class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            raise ValueError("Insufficient balance or invalid withdrawal amount.")

    def transfer(self, amount, recipient_account):
        if amount <= self.balance:
            self.withdraw(amount)
            recipient_account.deposit(amount)
            print(f"Transferred {amount} to account {recipient_account.account_number}")
        else:
            raise ValueError("Insufficient funds for transfer.")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, owner, initial_deposit=0):
        if account_number in self.accounts:
            raise ValueError("Account already exists.")
        else:
            new_account = Account(account_number, owner, initial_deposit)
            self.accounts[account_number] = new_account
            print(
                f"Account created for {owner} with account number {account_number}. Initial deposit: {initial_deposit}")

    def find_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Account not found.")

    def total_bank_balance(self):
        total_balance = sum(acc.balance for acc in self.accounts.values())
        print(f"Total balance across all accounts: {total_balance}")
        return total_balance


# Example usage of the Banking system
if __name__ == "__main__":
    my_bank = Bank("Global Trust Bank")

    my_bank.create_account(1001, "Alice", 500)
    my_bank.create_account(1002, "Bob", 300)

    alice_account = my_bank.find_account(1001)
    bob_account = my_bank.find_account(1002)

    alice_account.deposit(200)
    bob_account.withdraw(100)
    alice_account.transfer(150, bob_account)

    my_bank.total_bank_balance()