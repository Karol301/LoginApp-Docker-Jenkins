from database_manager import DatabaseManager

def main():
    db = DatabaseManager()

    login = input("Enter login: ")
    password = input("Enter password: ")

    if db.user_exists(login, password):
        print("User exists, logged in.")
    else:
        print("User does not exist. Adding user.")
        db.add_user(login, password)
        print(f"User {login} added.")

    db.close()

if __name__ == "__main__":
    main()
