"""
Проверяет были ли введены такие элементы при предыдущих запусках. Yes, если такие числа уже встречались, No - если таких чисел еще не было
"""

def factory():
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
    return yes_no

f1 = factory()
f1([1,2,1])
f1([1,2])
f1([1,2,3])
f1([1,2,3])
f1([4])
