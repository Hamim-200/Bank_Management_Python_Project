from bank import Bank
from user_customer import user_menu
from admin import admin_menu

bank = Bank()

while True:
    print("\n ====== Welcome to the ABCD Bank! ======")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter Your Choice: ").strip()
    if choice == '1':
        user_menu(bank)
    elif choice == '2':
        admin_menu(bank)
    elif choice == '3':
        print("Thank you for your Banking !!!")
        break
    else:
        print("Invalid Number. Please enter a number between 1 and 3.")
