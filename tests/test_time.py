import pandas as pd

from dsml_ai.time import create_lag_features, rolling_mean


def test_create_lag_features() -> None:
    s = pd.Series([1, 2, 3, 4])
    df = create_lag_features(s, [1, 2])
    assert list(df.columns) == ["lag_1", "lag_2"]
    assert pd.isna(df["lag_1"].iloc[0])
    assert df["lag_1"].iloc[1] == 1


def test_rolling_mean() -> None:
    s = pd.Series([1, 2, 3, 4])
    rm = rolling_mean(s, window=2)
    assert pd.isna(rm.iloc[0])
    assert rm.iloc[1] == 1.5
