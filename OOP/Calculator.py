def addition(*multiargs):
    total = 0
    for arg in multiargs:
        total += arg
    return total


def multiplication(*multiargs):
    total = 1
    for arg in multiargs:
        total *= arg
    return total



print(multiplication(1, 2, 3, 4, 5, 6, 7, 8, 9))