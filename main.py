"""
I want to create a simple python program to keep track of a user's balance.
I can deposit and withdraw money.
I can also create and view existing users.
"""
import json
bank_accounts = []


# Setting up the python program.
def run():
    load_data()
    print("==================================================")
    print("Welcome to Pickolzi's bank! How may we serve you!")
    commands()
    while True:
        user_option = input("")
        if user_option == "1":
            create_back_account()
        elif user_option == "2":
            delete_bank_account()
        elif user_option == "3":
            view_bank_account()
        elif user_option == "-1":
            save_data()
            print("Thank you for visiting Pickolzi's bank! Goodbye!")
            break
        else:
            print("Please select a valid option.")
            commands()


# Function to create a bank account.
def create_back_account():
    balance = 0
    while True:
        if balance != 0:
            commands()
            break
        new_member = input("Please give me a unique name to register your account. ")

        # Puts all the names of the dictionary bank account into one list variable.
        members = []
        for member in bank_accounts:
            members.append(member["name"])

        # Checks if the user signing up is not already part of the list.
        if new_member not in members:
            while True:
                try:
                    balance = float(input("What is your starting balance? "))
                    break
                except ValueError:
                    continue
            user_info = {"name": new_member,
                         "balance": balance
                         }
            bank_accounts.append(user_info)
            print("\n" + new_member)
            print("$" + str(balance))
        else:
            print("This bank account name already exists, please choose a different name! ")


# Function to delete a bank account.
def delete_bank_account():
    for x, bank_account in enumerate(bank_accounts):
        print(x+1, bank_account["name"])

    user_choose_bank_account = 0
    while True:
        try:
            user_choose_bank_account = int(input("Choose a bank account to delete by number. "))
            if user_choose_bank_account not in range(1, (len(bank_accounts) + 1)):
                continue
            else:
                break
        except ValueError:
            print("Please choose a valid bank account")

    index = user_choose_bank_account - 1
    delete_account = bank_accounts.pop(index)
    print(delete_account["name"], "has been deleted! ")
    commands()


# Function to view an existing bank account.
def view_bank_account():
    for x, bank_account in enumerate(bank_accounts):
        print(str(x+1) + ") " + bank_account["name"])

    user_choose_bank_account = 0
    while True:
        try:
            user_choose_bank_account = int(input("Choose a bank account to edit by number. "))
            if user_choose_bank_account not in range(1, (len(bank_accounts)+1)):
                continue
            else:
                break
        except ValueError:
            print("Please choose a valid bank account")

    index = user_choose_bank_account - 1
    message = "The user you selected: " + bank_accounts[index]["name"] + ", currently has $" + \
              str(bank_accounts[index]["balance"]) + " in their bank account!"
    print("==================================================")
    print(message)
    print("\nWhich action would you like to perform? ")
    print("1) Deposit money to your bank account.")
    print("2) Withdraw money from your bank account.")
    print("-1) Main menu.")
    print("==================================================")

    options = [-1, 1, 2]
    while True:
        try:
            user_choice = int(input("Which option would you like to perform? "))
            if user_choice not in options:
                continue
            else:
                break
        except ValueError:
            print("Please choose a valid option.")

    print("==================================================")
    if user_choice == 1:
        while True:
            try:
                user_money = float(input("How much would you like to deposit? "))
                if user_choice < 0:
                    print("Please don't enter a negative number")
                    continue
                else:
                    balance = bank_accounts[index]["balance"]
                    balance += user_money
                    bank_accounts[index]["balance"] = balance
                    break
            except ValueError:
                print("Please choose a valid option.")
    elif user_choice == 2:
        while True:
            try:
                user_money = float(input("How much would you like to withdraw? "))
                balance = bank_accounts[index]["balance"]
                if user_choice < 0:
                    print("Please don't enter a negative number")
                    continue
                elif user_money > balance:
                    print("The amount you're trying to withdraw is greater than your balance.")
                    continue
                else:
                    balance -= user_money
                    bank_accounts[index]["balance"] = balance
                    break
            except ValueError:
                print("Please choose a valid option.")
    commands()


# Function to display list of commands.
def commands():
    print("==================================================")
    print("Select one of these options")
    print("1) Create a new bank account")
    print("2) Delete a bank account")
    print("3) View an existing bank account")
    print("-1) EXIT")
    print("==================================================")


# Function to save the data.
def save_data():
    filename = "data.json"
    try:
        with open(filename, "w") as file:
            json.dump(bank_accounts, file, indent=4)
    except FileNotFoundError:
        print("File not found... Creating new file.")


# Function to load the data.
def load_data():
    filename = "data.json"
    try:
        with open(filename, "r") as file:
            global bank_accounts
            bank_accounts = json.load(file)
    except FileNotFoundError:
        print("No file could be found to load from....")

run()