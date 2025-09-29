"""
Time series analysis utilities.
"""

__all__ = ["create_lag_features", "rolling_mean"]

import pandas as pd

def create_lag_features(series: pd.Series, lags: list[int]) -> pd.DataFrame:
    """Generate a DataFrame of lagged features for a time series."""
    data = {f"lag_{lag}": series.shift(lag) for lag in lags}
    return pd.DataFrame(data)

def rolling_mean(series: pd.Series, window: int) -> pd.Series:
    """Compute the rolling mean over a specified window size."""
    return series.rolling(window=window).mean()
