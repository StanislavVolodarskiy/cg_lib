import itertools
import operator

from .core import area2


class GrahamScanner:
    def __init__(self, ccw=True, minimal=True):
        self._op = (
            (operator.gt if minimal else operator.ge)
            if ccw else
            (operator.lt if minimal else operator.le)
        )
        self.stack = []

    def append(self, p):
        while (len(self.stack) >= 2):
            if self._op(area2(self.stack[-2], self.stack[-1], p), 0):
                break
            self.stack.pop()
        self.stack.append(p)


def graham(points, minimal=True):
    sorted_points = sorted(points)
    if len(sorted_points) <= 2:
        return sorted_points

    # split points into sets below and above (left, right) line
    left = sorted_points[0]
    right = sorted_points[-1]
    below = GrahamScanner(ccw=True, minimal=minimal)
    above = GrahamScanner(ccw=False, minimal=minimal)

    above.append(left)
    for p in sorted_points:
        (below if area2(left, right, p) <= 0 else above).append(p)
    above.append(right)

    below.stack.extend(itertools.islice(
        reversed(above.stack), 1, len(above.stack) - 1
    ))

    return below.stack
