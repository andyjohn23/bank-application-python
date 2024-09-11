import sqlite3


def create_new_database():
    db_connection = sqlite3.connect("bank_of_moringa.db")
    db_cursor = db_connection.cursor()
    db_cursor = db_cursor.execute(
        "CREATE TABLE IF NOT EXISTS bank_users(id INTEGER PRIMARY KEY AUTOINCREMENT, owners_name TEXT NOT NULL, location TEXT NOT NULL, account_number INTEGER NOT NULL)")
    db_connection.commit()


def register_new_account():
    owner_name = input("Enter you fullname: ")
    location = input("Enter your location: ")
    account_number = input("Enter account number: ")

    db_connection = sqlite3.connect("bank_of_moringa.db")
    db_cursor = db_connection.cursor()
    db_cursor = db_cursor.execute(
        "SELECT * FROM bank_users WHERE account_number = ?", (account_number,))
    results = db_cursor.fetchone()
    db_connection.close()

    if results:
        print("Account already exists!!!")
    else:
        db_connection = sqlite3.connect("bank_of_moringa.db")
        db_cursor = db_connection.cursor()
        db_cursor = db_cursor.execute(
            "INSERT INTO bank_users(owners_name, location, account_number) VALUES(?, ?, ?)", (owner_name, location, account_number))
        db_connection.commit()
        db_connection.close()
        print(
            f"account for {owner_name} has been created successfully, account number is {account_number}")


class BankApplication:
    def __init__(self, owners_name, location, account_number):
        self.owners_name = owners_name
        self.location = location
        self.account_number = account_number

    def __str__(self):
        return f"Account for {self.owners_name} has been created successfully, and account number is {self.account_number}"


def main():
    create_new_database()

    print("Welcome to bank of moringa application")

    while True:
        print("Menu options")
        print("1. Create an account")
        print("2. Exit")

        menu_options = input("Choose from menu options: ")

        if menu_options == "1":
            register_new_account()
        elif menu_options == "2":
            break
        else:
            print("Invalid option, choose correct option again.")


if __name__ == "__main__":
    main()
