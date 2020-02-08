from cg_lib import convex_hull


def test_graham():
    graham = convex_hull.graham
    assert graham([(0, 0)]) == [(0, 0)]
    assert graham([(0, 0), (0, 1)]) == [(0, 0), (0, 1)]
    assert graham([(0, 0), (1, 0), (0, 1)]) == \
        [(0, 0), (1, 0), (0, 1)]
    assert graham([(0, 0), (1, 0), (2, 0)]) == \
        [(0, 0), (2, 0)]
    assert graham([(0, 0), (1, 0), (2, 0)], minimal=False) == \
        [(0, 0), (1, 0), (2, 0)]

    def line(x1, x2, y):
        return [(x, y) for x in range(x1, x2 + 1)]

    square = line(0, 2, 0) + line(0, 2, 1) + line(0, 2, 2)
    square_min_hull = [(0, 0), (2, 0), (2, 2), (0, 2)]
    square_max_hull = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
        (1, 2),
        (0, 2),
        (0, 1)
    ]

    assert graham(square) == square_min_hull
    assert graham(square, minimal=True) == square_min_hull
    assert graham(square, minimal=False) == square_max_hull

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

    assert graham(octagon) == octagon_min_hull
    assert graham(octagon, minimal=True) == octagon_min_hull
    assert graham(octagon, minimal=False) == octagon_max_hull

    bug = [
        (0, 1),
        (2, 0),
        (2, 1),
        (1, 1)
    ]
    assert graham(bug, minimal=False) == bug

    bug = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1)
    ]
    assert graham(bug, minimal=False) == bug
