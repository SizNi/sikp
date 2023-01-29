# создание понятие пары и обращение к ее элементам
def cons(a, b):
    def f(message):
        if message == "car":
            return a
        if message == "cdr":
            return b
    return f

def car(pair):
    return pair("car")

def cdr(pair):
    return pair("cdr")