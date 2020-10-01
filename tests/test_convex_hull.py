from cg_lib.convex_hull import graham


def test_graham():

    def triple_test(src, dst, max_dst=None):
        if max_dst is None:
            max_dst = dst

        def check(src, min_dst, max_dst):
            assert graham(src) == min_dst
            assert graham(src, minimal=True) == min_dst
            assert graham(src, minimal=False) == max_dst

        check(src, dst, max_dst)
        check(tuple(src), dst, max_dst)

        decor = {}
        for p in src:
            assert p not in decor
            decor[p] = p[0], p[1], len(decor)

        def decorate(points):
            return [decor[p] for p in points]

        dsrc = decorate(src)
        ddst = decorate(dst)
        dmax_dst = decorate(max_dst)

        check(dsrc, ddst, dmax_dst)
        check(tuple(dsrc), ddst, dmax_dst)

    triple_test(
        [],
        []
    )

    triple_test(
        [(0, 0)],
        [(0, 0)]
    )

    triple_test(
        [(0, 0), (0, 1)],
        [(0, 0), (0, 1)]
    )

    triple_test(
        [(0, 0), (1, 0), (0, 1)],
        [(0, 0), (1, 0), (0, 1)]
    )

    triple_test(
        [(0, 0), (1, 0), (2, 0)],
        [(0, 0), (2, 0)],
        [(0, 0), (1, 0), (2, 0), (1, 0)]
    )

    def line(x1, x2, y):
        return [(x, y) for x in range(x1, x2 + 1)]

    triple_test(
        line(0, 2, 0) + line(0, 2, 1) + line(0, 2, 2),
        [(0, 0), (2, 0), (2, 2), (0, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    )

    octagon = (
        line(2, 4, 0) +
        line(1, 5, 1) +
        line(0, 6, 2) +
        line(0, 6, 3) +
        line(0, 6, 4) +
        line(1, 5, 5) +
        line(2, 4, 6)
    )

    octagon_min_hull = [
        (0, 2),
        (2, 0),
        (4, 0),
        (6, 2),
        (6, 4),
        (4, 6),
        (2, 6),
        (0, 4)
    ]
    octagon_max_hull = [
        (0, 2),
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 1),
        (6, 2),
        (6, 3),
        (6, 4),
        (5, 5),
        (4, 6),
        (3, 6),
        (2, 6),
        (1, 5),
        (0, 4),
        (0, 3)
    ]

    triple_test(
        octagon,
        octagon_min_hull,
        octagon_max_hull
    )

    triple_test(
        [(0, 1), (2, 0), (2, 1), (1, 1)],
        [(0, 1), (2, 0), (2, 1)],
        [(0, 1), (2, 0), (2, 1), (1, 1)]
    )

    triple_test(
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 0), (2, 0), (2, 1)],
        [(0, 0), (1, 0), (2, 0), (2, 1)]
    )
