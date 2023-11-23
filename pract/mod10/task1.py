import re


def validate_password(password):
    """
        Данный метод проверяет корректность паролей

        >>> validate_password("rtG3FG!Tr^e")
        True
        >>> validate_password("aA1!*!1Aa")
        True
        >>> validate_password("oF^a1D@y5e6")
        True
        >>> validate_password("enroi#$rkdeR#$092uWedchf34tguv394h")
        True

        >>> validate_password("пароль")
        False
        >>> validate_password("password")
        False
        >>> validate_password("qwerty1")
        False
        >>> validate_password("lOngPa$$$W0Rd")
        False
        """
    if len(password) < 6:
        return False

    if not re.match("^[A-Za-z0-9^$%@#&*!?]*$", password):
        return False

    if len(re.findall("[A-Z]", password)) < 2:
        return False

    if not re.search("[0-9]", password):
        return False

    special_chars = re.findall("[^$%@#&*!?]", password)
    if len(set(special_chars)) < 2:
        return False

    if re.search(r"(.)\1\1", password):
        return False

    return True
