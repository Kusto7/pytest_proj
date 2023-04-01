from utils import dicts


def test_dicts():
    assert dicts.get_val({1: 'test1', 2: 'test2'}, 2)
    assert dicts.get_val({1: 'test1', 2: 'test2'}, 1)
    assert dicts.get_val({1: 'test1', 2: 'test2'}, 0)
    assert dicts.get_val({}, 1)
    assert dicts.get_val({}, 1, 'yes')
