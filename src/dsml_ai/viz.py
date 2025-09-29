"""
Visualization utilities for data exploration and results presentation.
"""

__all__ = ["plot_histogram", "plot_correlation_matrix"]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(
    data: np.ndarray | pd.Series, bins: int = 10
) -> plt.Figure:
    """Plot a histogram of the data and return the Figure."""
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins)
    return fig

def plot_correlation_matrix(df: pd.DataFrame) -> plt.Figure:
    """Plot a correlation matrix heatmap for a DataFrame and return the Figure."""
    corr = df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, ax=ax, annot=True)
    return fig
