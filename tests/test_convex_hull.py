from cg_lib import convex_hull


def test_graham():
    assert convex_hull.graham([(0, 0)]) == [(0, 0)]
    assert convex_hull.graham([(0, 0), (1, 0), (0, 1)]) == \
        [(0, 0), (1, 0), (0, 1)]
