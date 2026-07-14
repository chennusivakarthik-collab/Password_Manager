import getpass
import hashlib

password_manager = {}

def create_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in password_manager and password_manager[username] == hashed_password:
        print("Login successful")
    else:
        print("Invalid credentials")

def main():
    while True:
        choice = input("Enter 1 to create account, 2 to login, or 0 to exit: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if _name_ == "_main_":
    main()