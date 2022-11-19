from random import randint

def representate():
    state = validate()
    if state == 0:
        # put number in nX
        pass
    elif state == 1:
        #put number in nY
        pass
    else:
        # put nY in nX && put number in nY
        pass


def generate_all(start: int, end: int)-> int:
    return randint(start, end)


def generate_par(start: int, end: int)-> int:
    nb = 1
    while nb % 2 != 0:
        nb = randint(start, end)
    return nb


def generate_impar(start: int, end: int)-> int:
    nb = 0
    while nb % 2 == 0:
        nb = randint(start, end)
    return nb


def validate():
    # check for representation position
    if nX == 0:
        return 0
    elif nY == 0:
        return 1
    else:
        return 2


# initial values declaration
buffer = 0
nX = 0
nY = 0