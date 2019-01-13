
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
