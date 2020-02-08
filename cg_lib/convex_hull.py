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
    on_line = []
    above = GrahamScanner(ccw=False, minimal=minimal)

    above.append(left)
    on_line.append(left)
    below.append(left)
    for p in itertools.islice(sorted_points, 1, len(sorted_points) - 1):
        a2 = area2(left, right, p)
        if a2 < 0:
            below.append(p)
        if a2 > 0:
            above.append(p)
        if a2 == 0 and not minimal:
            on_line.append(p)
    above.append(right)
    on_line.append(right)
    below.append(right)

    below_envelope = below.stack
    above_envelope = above.stack
    if len(below.stack) == 2:
        below_envelope = on_line
    elif len(above.stack) == 2:
        above_envelope = on_line

    below_envelope.extend(itertools.islice(
        reversed(above_envelope), 1, len(above_envelope) - 1
    ))
    return below_envelope
