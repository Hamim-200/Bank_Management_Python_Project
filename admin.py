def admin_menu(bank):
    admin = bank.manage_admin_actions()
    while True:
        print("\n-----Admin-----")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. All Accounts List")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan Feature")
        print("7. Dashboard")
        choice = input("Enter Your Choice: ").strip()

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Savings or Cuurent): ")
            user = admin.create_account(name, email, address, account_type)
            print(f"Your Account created successfully. Your account number is {user.account_number}")

        elif choice == '2':
            account_number = int(input("Enter account number to delete: "))
            result = admin.delete_account(account_number)
            print(result)

        elif choice == '3':
            accounts = admin.list_all_accounts()
            print("List of all accounts:")
            for user in accounts:
                print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}")

        elif choice == '4':
            total_balance = admin.check_total_balance()
            print(f"Total balance in the bank: {total_balance}")

        elif choice == '5':
            total_loan_amount = admin.check_total_loan_amount()
            print(f"Total loan amount: {total_loan_amount}")

        elif choice == '6':
            result = admin.toggle_loan_feature()
            print(result)
        elif choice == '7':
            break
        else:
            print("Invalid Number. Please enter a number between 1 and 7.")