def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 4, 1, 1,))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)