def bread(f):
    def wrap(*args):
        print("</------------\\>")
        f(*args)
        print("<\\____________/>")

    return wrap


def tomato(f):
    def wrap(*args):
        print("*** помидоры ****")
        f(*args)

    return wrap


def onion(f):
    def wrap(*args):
        print("----- лук ------")
        f(*args)

    return wrap


def salad(f):
    def wrap(*args):
        print("~~~~ салат ~~~~~")
        f(*args)

    return wrap


def cheese(f):
    def wrap(*args):
        print("^^^^^ сыр ^^^^^^")
        f(*args)

    return wrap


# hamburger
@bread
@onion
@tomato
def beef():
    print("### говядина ###")


beef()

print("==================================")


# hamburger
@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")


chicken()
