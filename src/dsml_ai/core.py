"""
Core utilities for data science and machine learning workflows.
"""

__all__ = ["train_test_split", "encode_categorical"]

import pandas as pd
from sklearn.model_selection import train_test_split as _sk_train_test_split

def train_test_split(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int | None = None
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split a DataFrame into train and test sets."""
    return _sk_train_test_split(df, test_size=test_size, random_state=random_state)

def encode_categorical(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """One-hot encode specified categorical columns in a DataFrame."""
    return pd.get_dummies(df, columns=columns)
