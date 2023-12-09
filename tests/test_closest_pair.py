import pytest
from cg_lib.closest_pair import closest_pair


def test_closest_pair():
    with pytest.raises(AssertionError):
        closest_pair(())

    with pytest.raises(AssertionError):
        closest_pair(((0, 0), ))

    for n in range(2, 10):
        assert closest_pair(tuple((i, i * i) for i in range(n))) == \
            ((0, 0), (1, 1))

    assert closest_pair(((0, 2), (0, 3), (1, 0), (1, 4))) == ((0, 2), (0, 3))
    assert closest_pair(((9, 0), (2, 0), (8, 7), (3, 5))) == ((2, 0), (3, 5))

    assert closest_pair(((0, 0), (1, 0), (1, 1), (0, 1), (0, 0))) == \
        ((0, 0), (0, 0))

    assert closest_pair(((0, 0), ) * 100) == ((0, 0), ) * 2
