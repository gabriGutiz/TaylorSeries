from ..TaylorSeries.TaylorSeries import TSsin
import math

def test_sin():
    result = TSsin(math.pi, 10)

    assert result == math.sin(math.pi)

if __name__ == '__main__':
    test_sin()