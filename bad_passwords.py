from string import digits

data = ["1234", "qwerty", "123qwerty"]


def check_password(value):
    value = str(value)

    def decorator(func):
        def wrapper():
            return func()

        return wrapper

    def check_len_password():
        length = len(value)
        if 12 >= length >= 6:
            return [True, 1]
        return [False, ValueError("Недопустимая длина пароля ;с")]

    def check_digits_in_password():
        for char in value:
            if char in digits:
                return [True, 1]
        return [False, ValueError("Нет цифр ;с")]

    def check_bad_passwords():
        if value not in data:
            return [True, 1]
        return [False, ValueError("Плохой пароль ;с")]

    checks_function = [check_len_password, check_digits_in_password, check_bad_passwords]
    for current_func in checks_function:
        verdict = decorator(current_func)()
        if False in verdict:
            return verdict
    return [True, 1]
