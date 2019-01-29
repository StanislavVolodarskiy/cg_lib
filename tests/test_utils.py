from six.moves import range, zip

from cg_lib import utils


def test_cyclic_pairs():
    assert list(utils.cyclic_pairs([])) == []
    assert list(utils.cyclic_pairs([0])) == [(0, 0)]
    assert list(utils.cyclic_pairs([0, 1])) == [(0, 1), (1, 0)]
    assert list(utils.cyclic_pairs([0, 1, 2])) == [(0, 1), (1, 2), (2, 0)]
    assert list(utils.cyclic_pairs(range(10))) == \
        list(zip(range(10), list(range(1, 10)) + [0]))
