"""
Проверяет были ли введены такие элементы при предыдущих запусках. Yes, если такие числа уже встречались, No - если таких чисел еще не было
"""
s = set()


def yes_no(l):
    if len(s) == 0:
        s.update(l)
        if len(l) == len(s):
            print("No")
        else:
            print("Yes")
    else:
        old_size = len(s)
        s.update(l)
        new_size = len(s)
        if old_size == new_size:
            print("Yes")
        else:
            print("No")


yes_no([1, 2, 1])
yes_no([1, 2])
yes_no([4, 2])
yes_no([3])
yes_no([1, 2, 1, 3, 4])
