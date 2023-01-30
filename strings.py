def cons(a, b):
    return f"{a}\\0{b}"

def car(pair):
    return pair[:pair.find("\\0")]

def cdr(pair):
    return pair[pair.find("\\0")+2:]
