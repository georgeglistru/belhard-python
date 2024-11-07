def rubles_str(rubles, cop):
    if rubles > 1000:
        raise ValueError("Поддерживается только до 1000 рублей")
    if cop > 99:
        raise ValueError("Копеек не может быть больше 99")

    res = ""
    if rubles in (1,):
        res += f"{rubles} рубль"
    elif rubles in (2, 3, 4):
        res += f"{rubles} рубля"
    elif rubles in range(5, 21):
        res += f"{rubles} рублей"
    elif rubles % 100 in range(11, 20):
        res += f" {rubles} рублей"
    elif rubles % 10 in (1,):
        res += f" {rubles} рубль"
    elif rubles % 10 in (2, 3, 4):
        res += f" {rubles} рубля"
    else:
        res += f" {rubles} рублей"

    if cop == 0:
        res += ""
    elif cop in (1,):
        res += f" {cop} копейка"
    elif cop in (2, 3, 4):
        res += f" {cop} копейки"
    elif cop in (5, 6, 7, 8, 9, 10):
        res += f" {cop} копеек"
    elif cop in range(5, 21):
        res += f" {cop} копеек"
    elif cop % 10 == 1:
        res += f" {cop} копейка"
    elif cop % 10 in (2, 3, 4):
        res += f" {cop} копейки"
    else:
        res += f" {cop} копеек"

    return res


r = int(input("Введите кол-во рублей "))
c = int(input("Введите кол-во копеек "))
print(rubles_str(r, c))

# print(rubles_str(1,0))
# print(rubles_str(1,1))
# print(rubles_str(2,0))
# print(rubles_str(2,2))
# print(rubles_str(3,3))
# print(rubles_str(4,4))
# print(rubles_str(5,5))
# print(rubles_str(6,6))
# print(rubles_str(7,7))
# print(rubles_str(8,8))
# print(rubles_str(9,9))
# for _ in range(0, 100) :
#     print(rubles_str(10, _))
# for _ in range(0, 1001) :
#     print(rubles_str(_, 1))
