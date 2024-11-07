def str_val(s):
    res = dict()
    for ch in s:
        if ch in res:
            res[ch] += 1
        else:
            res[ch] = 1
    return res


print(str_val("python is the fastest-growing major programming language"))
