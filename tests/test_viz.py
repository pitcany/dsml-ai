import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dsml_ai.viz import plot_histogram, plot_correlation_matrix


def test_plot_histogram() -> None:
    data = np.array([1, 2, 2, 3])
    fig = plot_histogram(data, bins=3)
    assert isinstance(fig, plt.Figure)
    ax = fig.axes[0]
    # Should produce three bars
    assert len(ax.patches) == 3


def test_plot_correlation_matrix() -> None:
    df = pd.DataFrame({"x": [1, 2, 3], "y": [3, 2, 1]})
    fig = plot_correlation_matrix(df)
    assert isinstance(fig, plt.Figure)
    ax = fig.axes[0]
    # Heatmap should have a QuadMesh or similar collection
    assert ax.collections
