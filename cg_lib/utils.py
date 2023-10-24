import itertools


def pairs(seq):
    it1, it2 = itertools.tee(seq)
    next(it2, None)
    return zip(it1, it2)


def cyclic_pairs(seq):
    it = iter(seq)
    try:
        first = next(it)
    except StopIteration:
        return
    prev = first
    for item in it:
        yield prev, item
        prev = item
    yield prev, first
