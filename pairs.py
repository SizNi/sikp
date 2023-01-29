import math

# нахождение простых делителей


def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


# реализация через функции
def cons(a, b):
    return 2 ** a * 3 ** b


def car(pair):
    return primfacs(pair).count(2)


def cdr(pair):
    return primfacs(pair).count(3)


# реализаия через лямбда-функции
def cons(x, y):
    return lambda result: result(2**x, 3**y)


def car(fn):
    return round(math.log(fn(lambda x, _: x), 2))


def cdr(fn):
    return round(math.log(fn(lambda _, y: y), 3))
