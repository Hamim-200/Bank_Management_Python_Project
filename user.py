def user_menu(bank):
     while True:
        print("\nUSER MENU")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Check Transaction History")
        print("6. Take a Loan")
        print("7. Transfer Money")
        print("8. Dashboard")
        choice = input("Enter Your Choice: ").strip()

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Savings or Cuurent): ")
            admin = bank.manage_admin_actions()
            user = admin.create_account(name, email, address, account_type)
            print(f"Your Account created successfully. Your account number is {user.account_number}")

        elif choice == '2':
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter Deposit Amount: "))
            if account_number in bank.user_accounts:
                bank.user_accounts[account_number].deposit(amount)
                print("Amount deposited successfully.")
            else:
                print("Account does not exist")

        elif choice == '3':
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter amount to withdraw: "))
            if account_number in bank.user_accounts:
                result = bank.user_accounts[account_number].withdraw(amount)
                print(result)
            else:
                print("Account does not exist..")

        elif choice == '4':
            account_number = int(input("Enter your account number: "))
            if account_number in bank.user_accounts:
                balance = bank.user_accounts[account_number].check_balance()
                print(f"Available balance: {balance}")
            else:
                print("Account does not exist..")

        elif choice == '5':
            account_number = int(input("Enter your account number: "))
            if account_number in bank.user_accounts:
                history = bank.user_accounts[account_number].check_transaction_history()
                print("==============Transaction History==========:")
                for transaction in history:
                    print(transaction)
            else:
                print("Account does not exist..")

        elif choice == '6':
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter loan amount: "))
            if account_number in bank.user_accounts:
                result = bank.user_accounts[account_number].take_loan(amount)
                print(result)
            else:
                print("Account does not exist..")

        elif choice == '7':
            from_account = int(input("Enter your account number: "))
            to_account = int(input("Enter the account number to transfer to: "))
            amount = float(input("Enter amount to transfer: "))
            if from_account in bank.user_accounts and to_account in bank.user_accounts:
                result = bank.user_accounts[from_account].transfer_amount(bank.user_accounts[to_account], amount)
                print(result)
            else:
                print("Accounts not found.")

        elif choice == '8':
            break
        else:
            print("Invalid Number. Please enter a number between 1 and 8.")