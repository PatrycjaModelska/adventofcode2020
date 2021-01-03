# generator wszystkich podzbiorów

def powerset(xs):
    if len(xs) <= 1:
        yield xs
        yield []
    else:
        for item in powerset(xs[1:]):
            yield item
            yield [xs[0]] + item

