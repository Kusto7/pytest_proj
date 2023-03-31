from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([], 4) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7], -4) == [4, 5, 6, 7]
    assert arrs.my_slice([-1, -2, -3, -4, -5, -6, -7], -4) == [-4, -5, -6, -7]
    assert arrs.my_slice([-1, -2, -3, -4, -5, -6, -7], 4) == [-5, -6, -7]
    assert arrs.my_slice([-1, -2, -3, -4, -5, -6, -7], 0) == [-1, -2, -3, -4, -5, -6, -7]
    assert arrs.my_slice([], -4) == []
