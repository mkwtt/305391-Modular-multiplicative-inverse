import pytest

from src.algorithms.MMI import extendedEuclidean


@pytest.mark.parametrize(
    "a, m, inverse",
    [
        (3, 7, 5),
        (60, 48, None),
    ],
)
def test_MMI(a, m, inverse):
    result = extendedEuclidean(a, m)

    assert result == inverse
