def yes_no(l):
    """Yes, если есть дубликаты, No, если все значения уникальны"""
    s = set(l)
    if len(l) == len(s):
        print("No")
    else:
        print("Yes")


yes_no([1, 2])
yes_no([1, 1])
yes_no([1, -1])
yes_no([1, -1, 1, 2, 3])
