import numpy as np
import pytest
from dsml_ai.stats import (
    linear_regression,
    LinRegResult,
    ttest_ind,
    ttest_rel,
    ttest_1samp,
)


def test_linear_regression_perfect_fit() -> None:
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    result = linear_regression(x, y)
    assert isinstance(result, LinRegResult)
    assert pytest.approx(result.slope, rel=1e-6) == 2.0
    assert pytest.approx(result.intercept, rel=1e-6) == 0.0
    assert pytest.approx(result.r_value, rel=1e-6) == 1.0
    assert pytest.approx(result.p_value, rel=1e-6) == 0.0
    assert pytest.approx(result.std_err, rel=1e-6) == 0.0

def test_ttest_ind_same_samples() -> None:
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    stat, p = ttest_ind(a, b)
    assert pytest.approx(stat, abs=1e-6) == 0.0
    assert pytest.approx(p, abs=1e-6) == 1.0

def test_ttest_rel_same_samples() -> None:
    a = [5, 6, 7]
    b = [5, 6, 7]
    stat, p = ttest_rel(a, b)
    # Identical paired samples produce NaN due to zero variance
    assert np.isnan(stat)
    assert np.isnan(p)

def test_ttest_1samp_zero_mean() -> None:
    a = [1.0, -1.0, 2.0, -2.0]
    stat, p = ttest_1samp(a, popmean=0.0)
    assert pytest.approx(stat, abs=1e-6) == 0.0
    assert pytest.approx(p, abs=1e-6) == 1.0
