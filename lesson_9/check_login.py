import re


def check_login(login: str) -> bool:
    """
Проверяет, что логин, который соответствует следующим правилам:
1. Длина от 5 до 20 символов
2. Состоит из букв верхнего и нижнего регистра, цифр, знаков подчеркивания
    :param login:
    :return: true, если удовлетворяет правилам, false если нет
    """
    if re.match("^[a-zA-Z0-9_]{5,20}$", login):
        return True
    else:
        return False


print(check_login("1234"))
print(check_login("12345"))
print(check_login("12345678901234567890"))
print(check_login("123456789012345678901"))
print(check_login("abAC1_"))
print(check_login("abAC1_!"))
print(check_login(",abAC1_"))
