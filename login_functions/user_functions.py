import hash_function

class user:
    def __init__(self):
        pass

    def login(self, username, password):
        with open("dummy_data_users.txt") as file:
            for line in file:
                user, passw = line.split(",")
                if str(username) == str(user) and str(hash(password)) == str(passw):
                    return True
        return False

    def register(self, username, password):
        pass

User = user()
print(User.login("jackt", "password1!"))
