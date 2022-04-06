def sum(nr):
    sum = 0
    for i in range(0, nr + 1):
        sum += i
    return sum


def sum_pare(nr):
    sum = 0
    for i in range(0, nr + 1):
        if (i % 2 == 0):
            sum += i
    return sum


def sum_impare(nr):
    sum = 0
    for i in range(0, nr + 1):
        if (i % 2 != 0):
            sum += i
    return sum
