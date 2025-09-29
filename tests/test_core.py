import pandas as pd

from dsml_ai.core import train_test_split, encode_categorical


def test_train_test_split() -> None:
    df = pd.DataFrame({"a": list(range(10))})
    train, test = train_test_split(df, test_size=0.3, random_state=0)
    assert len(train) == 7
    assert len(test) == 3
    # Ensure train and test are disjoint
    assert set(train['a']).isdisjoint(set(test['a']))


def test_encode_categorical() -> None:
    df = pd.DataFrame({"cat": ["a", "b", "a"], "num": [1, 2, 3]})
    result = encode_categorical(df, ["cat"])
    assert "cat_a" in result.columns and "cat_b" in result.columns
    assert result["cat_a"].tolist() == [1, 0, 1]
