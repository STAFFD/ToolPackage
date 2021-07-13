def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@parametrized
def printBefore(func, arg):
    def func_wrapper(*args, **kw):
        print(arg)
        func(*args, **kw)
    return func_wrapper


@printBefore("Here is a one-million-dollar equation:")
def addUp(x, y):
    print("{}+{}={}".format(x, y, x+y))

if __name__ == "__main__":
    addUp(1, 1)