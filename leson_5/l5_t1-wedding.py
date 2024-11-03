def where_wedding(guests):
    print(f"guests {guests}")
    if guests > 50:
        return "restaraunt"
    elif guests >= 20:
        return "cafe"
    else:
        return "at home"

print(where_wedding(51))
print(where_wedding(50))
print(where_wedding(49))
print(where_wedding(21))
print(where_wedding(20))
print(where_wedding(19))
