"""
Statistical analysis utilities.
"""
from __future__ import annotations

__all__ = [
    "LinRegResult",
    "linear_regression",
    "ttest_ind",
    "ttest_rel",
    "ttest_1samp",
]

from typing import Sequence
import numpy as np
from scipy import stats
from dataclasses import dataclass


@dataclass
class LinRegResult:
    """Result of a simple linear regression."""
    slope: float
    intercept: float
    r_value: float
    p_value: float
    std_err: float


def linear_regression(
    x: Sequence[float] | np.ndarray, y: Sequence[float] | np.ndarray
) -> LinRegResult:
    """
    Perform simple linear regression on x and y.

    Returns a LinRegResult containing slope, intercept, r_value, p_value, and std_err.
    """
    result = stats.linregress(x, y)
    return LinRegResult(
        slope=result.slope,
        intercept=result.intercept,
        r_value=result.rvalue,
        p_value=result.pvalue,
        std_err=result.stderr,
    )


def ttest_ind(
    a: Sequence[float] | np.ndarray,
    b: Sequence[float] | np.ndarray,
    equal_var: bool = True,
) -> stats.TtestResult:
    """
    Perform independent two-sample t-test.

    Parameters:
        a, b: Arrays of sample observations.
        equal_var: If True (default), perform standard independent t-test.
                   If False, perform Welch's t-test.

    Returns:
        A TtestResult with statistic and pvalue.
    """
    return stats.ttest_ind(a, b, equal_var=equal_var)


def ttest_rel(
    a: Sequence[float] | np.ndarray,
    b: Sequence[float] | np.ndarray,
) -> stats.TtestResult:
    """
    Perform paired two-sample t-test.

    Parameters:
        a, b: Arrays of sample observations (paired).

    Returns:
        A TtestResult with statistic and pvalue.
    """
    return stats.ttest_rel(a, b)


def ttest_1samp(
    a: Sequence[float] | np.ndarray, popmean: float = 0.0
) -> stats.TtestResult:
    """
    Perform one-sample t-test against a population mean.

    Parameters:
        a: Array of sample observations.
        popmean: Population mean to test against (default 0.0).

    Returns:
        A TtestResult with statistic and pvalue.
    """
    return stats.ttest_1samp(a, popmean)
