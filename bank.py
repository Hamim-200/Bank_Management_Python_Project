class User:
    account_number_counter = 1000
    
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = User.account_number_counter
        User.account_number_counter += 1
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal amount exceeded"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            return "Withdrawal successful"
        
    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transaction_history.append(f"Loan taken: {amount}")
            return "Loan Confirmed"
        else:
            return "Loan limit crossed"
        
    def transfer_amount(self, target_user, amount):
        if amount > self.balance:
            return "Transfer amount exceeded"
        else:
            self.balance -= amount
            target_user.balance += amount
            self.transaction_history.append(f"Transferred {amount} to account {target_user.account_number}")
            target_user.transaction_history.append(f"Received {amount} from account {self.account_number}")
            return "Transfer successful"
        
class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.bank.user_accounts[user.account_number] = user
        return user

    def delete_account(self, account_number):
        if account_number in self.bank.user_accounts:
            del self.bank.user_accounts[account_number]
            return "Account deleted"
        else:
            return "Account does not exist"

    def list_all_accounts(self):
        return list(self.bank.user_accounts.values())

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.bank.user_accounts.values())
        return total_balance

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.loan_count * user.balance for user in self.bank.user_accounts.values())
        return total_loan_amount

    def toggle_loan_feature(self):
        self.bank.loan_feature_enabled = not self.bank.loan_feature_enabled
        return "Loan feature enabled" if self.bank.loan_feature_enabled else "Loan feature disabled"
    
class Bank:
    def __init__(self):
        self.user_accounts = {}
        self.total_balance = 0
        self.total_loans = 0
        self.loan_feature_enabled = True

    def manage_user_accounts(self):
        return self.user_accounts

    def manage_admin_actions(self):
        return Admin(self)