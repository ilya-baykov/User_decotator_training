from bad_passwords import check_password


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        result = check_password(value)
        if True in result:
            self.__password = value
        else:
            raise result[1]


t1 = User("ilya", "8V4PM234")
print(t1.password)
