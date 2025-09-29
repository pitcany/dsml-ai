import numpy as np

from dsml_ai.dl import relu, softmax


def test_relu() -> None:
    x = np.array([-1, 0, 2])
    out = relu(x)
    assert np.array_equal(out, np.array([0, 0, 2]))


def test_softmax() -> None:
    x = np.array([0.0, np.log(2), np.log(3)])
    out = softmax(x)
    expected = np.array([1, 2, 3]) / 6
    assert np.allclose(out, expected)
    assert np.isclose(out.sum(), 1.0)
