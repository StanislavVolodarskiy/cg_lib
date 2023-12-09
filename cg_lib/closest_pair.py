import math

from .core import dist2


def closest_pair(points):
    assert len(points) >= 2
    points = sorted(points)

    threshold = 4  # TODO: select by performance tests
    assert threshold >= 4

    def make_pair(p1, p2):
        return dist2(p1, p2), p1, p2

    def closest_pair(n1, n2, yp):
        if n2 - n1 < threshold:
            return min(
                make_pair(points[i], points[j])
                for i in range(n1, n2 - 1)
                for j in range(i + 1, n2)
            )

        n = (n1 + n2) // 2
        pn = points[n]
        if points[n - 1][:2] == pn[:2]:
            return 0, points[n - 1], pn

        yp_l = []
        yp_r = []
        for p in yp:
            (yp_l if p < pn else yp_r).append(p)

        cp = min(closest_pair(n1, n, yp_l), closest_pair(n, n2, yp_r))

        dmax = math.isqrt(cp[0])
        if dmax * dmax == cp[0]:
            dmax -= 1

        xmax = points[n][0] + dmax
        xmin = points[n][0] - dmax

        bp = [p for p in yp if xmin <= p[0] <= xmax]
        m = len(bp)

        for i, pi in enumerate(bp):
            ymax = pi[1] + dmax
            for j in range(i + 1, m):
                pj = bp[j]
                if pj[1] > ymax:
                    break
                cp = min(cp, make_pair(pi, pj))

        return cp

    return closest_pair(0, len(points), sorted(points, key=lambda p: p[1]))[1:]
