class User:

    users = []

    def __init__(self, firstName, secondName, password):
        self.firstName = firstName
        self.secondName = secondName
        self.password = password

    def save_user(self):
        User.users.append(self)

    @classmethod
    def display_users(cls):
        return cls.users

    @classmethod
    def find_by_name(cls, name):
        for user in cls.users:
            if user.firstName == name: 
                return user
