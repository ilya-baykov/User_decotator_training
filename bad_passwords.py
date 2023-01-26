from string import digits

data = ["123456", "dragon", "password", "123456789", "12345", "qwerty", "1234567", "qwertyuiop", "111111", "1234567890",
        "123123", "123321", "abc123", "1234", "password1", "iloveyou", "1q2w3e4r", "000000", "qwerty123", "zaq12wsx",
        "sunshine", "princess", "12345678", "letmein", "654321", "monkey", "27653", "1qaz2wsx", "superman",
        "asdfghjkl"],


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
