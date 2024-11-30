import re


def check_phone(phone: str) -> bool:
    """
Проверяет, что строка соответствует шаблону:
1. код страны +375
2. код оператора 29, 33, 44, 25 в скобках
3. три цифры
4. тире
5. две цифры
6. тире
7 две цифры
    :param phone:
    :return: true, если удовлетворяет правилам, false если нет
    """
    if re.match(r"^\+375\((29|33|44|25)\)\d{3}-\d{2}-\d{2}$", phone):
        return True
    else:
        return False


print(check_phone("1234"))
print(check_phone("+375(29)123-45-67"))
print(check_phone("+375(21)123-45-67"))
print(check_phone("+370(29)123-45-67"))
print(check_phone("+375(29)123-4567"))
print(check_phone("+375(29)12345-67"))
print(check_phone("+375(29123-45-67"))
print(check_phone("+375(29)123-45-67"))
print(check_phone("+375(29)123-45-678"))
print(check_phone("+375(29)1234-5-678"))
