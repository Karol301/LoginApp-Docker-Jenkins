class UserInterface:
    def get_credentials(self):
        login = input("Podaj login: ")
        password = input("Podaj hasło: ")
        return login, password
