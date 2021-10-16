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


def farthest(left, right, points):
    d = sub(right, left)

    def cmp_(p1, p2):
        p12 = sub(p2, p1)
        a = cross(d, p12)
        if a < 0:
            return -1
        if a > 0:
            return 1
        b = dot(d, p12)
        if b < 0:
            return -1
        if b > 0:
            return 1
        return 0

    return max(points, key=functools.cmp_to_key(cmp_))


def partition(left, top, right, points):
    lpoints = []
    rpoints = []
    for p in points:
        # TODO: performance
        if area2(left, top, p) > 0:
            lpoints.append(p)
        # TODO: performance
        elif area2(top, right, p) > 0:
            rpoints.append(p)
    return lpoints, rpoints


def envelope(hull, left, right, points):
    top = farthest(left, right, points)
    lpoints, rpoints = partition(left, top, right, points)
    envelope(hull, top, right, rpoints)
    hull.append(top)
    envelope(hull, left, top, lpoints)


def select_points(points, p1, p2):
    left = []
    right = []
    for p in points:
        # TODO: performance
        a = area2(p1, p2, p)
        if a > 0:
            left.append(p)
        elif a < 0:
            right.append(p)
    return left, right


def quick_hull_minimal(points):

    if len(points) <= 0:
        return []

    left = min(points)
    right = max(points)

    below, above = select_points(points, left, right)
    hull = [left]
    envelope(hull, left, right, below)
    hull.append(right)
    envelope(hull, right, left, above)
    return hull


