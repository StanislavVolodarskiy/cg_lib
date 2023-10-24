import itertools
import operator

from .core import area2


class GrahamScanner:
    def __init__(self, minimal=True):
        self._op = operator.gt if minimal else operator.ge
        self.stack = []
        self._protected = 1

    def protect(self):
        assert len(self.stack) > 0
        self._protected = len(self.stack)

    def clean(self, point):
        while len(self.stack) > self._protected:
            if self._op(area2(self.stack[-2], self.stack[-1], point), 0):
                break
            self.stack.pop()

    def append(self, point):
        self.clean(point)
        self.stack.append(point)

    def extend(self, points):
        for p in points:
            self.append(p)


def graham(points, minimal=True):
    if len(points) <= 0:
        return []

    sorted_points = sorted(points)

    scanner = GrahamScanner(minimal=minimal)
    scanner.extend(sorted_points)
    scanner.protect()
    scanner.extend(itertools.islice(
        reversed(sorted_points),
        1,
        len(sorted_points) - 1
    ))
    scanner.clean(sorted_points[0])

    return scanner.stack
