def recursive(func):
    def self(*arg, **kargs):
        return func(self, *arg, **kargs)
    return self

def tail_recursive(func):
    class recur(object):
        def __init__(self, *args, **kargs):
            self.args, self.kargs = args, kargs

        def __repr__(self):
            return "Recur({} {})".format(self.args, self.kargs)

    def run(*args, **kargs):
        rec = recur(*args, **kargs)
        while isinstance(rec, recur):
            rec = func(recur, *rec.args, **rec.kargs)
        return rec
    return run

# note tail_recur only works for tail call recution for
# arbatrary recurtion see the Y combinator
# https://en.wikiped ia.org/wiki/Fixed-point_combinator
ycombinator = lambda f: (lambda g: f(lambda *arg, **kargs: g(g)(*arg, **kargs))) \
                        (lambda g: f(lambda *arg, **kargs: g(g)(*arg, **kargs)))

yrecursive = lambda func: ycombinator(lambda self: lambda *arg, **kargs: func(self, *arg, **kargs))
