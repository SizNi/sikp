def cons_2(x, y):
    def f(message):
        if message == "car":
            return x
        if message == "cdr":
            return y
    return f


def cons(head, tail):
    return lambda selector: selector(head, tail)


# в функцию car передается функция pair
# в return вызывается переданная функция pair с двумя аргументами
# и возвращается один из них
def car(fn):
    return fn(lambda head, tail: head)


def cdr(fn):
    return fn(lambda head, tail: tail)
# END
