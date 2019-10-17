from cg_lib import core


def test_cross1():
    assert core.cross1((1, 2)) == (-2, 1)


def test_mul():
    assert core.mul((2, 3), 5) == (10, 15)


def test_sub():
    assert core.sub((4, 6), (3, 4)) == (1, 2)


def test_add():
    assert core.add((1, 2), (3, 4)) == (4, 6)


def test_dot():
    assert core.dot((1, 0), (0, 1)) == 0
    assert core.dot((0, 1), (1, 0)) == 0
    assert core.dot((1, 2), (3, 4)) == 11


def test_len2():
    assert core.len2((3, 4)) == 25


def test_dist2():
    assert core.dist2((3, 4), (5, 7)) == 13


def test_cross():
    assert core.cross((1, 0), (0, 1)) == 1
    assert core.cross((0, 1), (1, 0)) == -1
    assert core.cross((1, 2), (3, 4)) == -2


def test_area2():
    assert core.area2((0, 0), (1, 0), (0, 1)) == 1
    assert core.area2((0, 0), (0, 1), (1, 0)) == -1
    assert core.area2((3, 5), (4, 6), (2, 6)) == 2
