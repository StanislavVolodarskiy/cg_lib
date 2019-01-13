import operator

from .core import area2


def graham_scan(points, minimal=True):
    if len(points) <= 2:
        return points

    op = operator.le if minimal else operator.lt

    stack = []

    def scan(it):
        min_stack_len = len(stack) + 1
        prev = next(it)
        for p in it:
            stack.append(prev)
            while (
                len(stack) > min_stack_len and
                op(area2(stack[-2], stack[-1], p), 0)
            ):
                stack.pop()
            prev = p

    scan(iter(points))
    scan(reversed(points))
    return stack


def graham(points, minimal=True):
    return graham_scan(sorted(points), minimal=minimal)
